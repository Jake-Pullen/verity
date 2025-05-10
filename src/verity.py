import os
import logging
import logging.config
import atexit

from flask import Flask

from data_handler import database
from config import VerityConfig
from front.home import home_bp

def set_up_logging(config):
    os.makedirs('../logs', exist_ok=True)
    logging.config.dictConfig(config.LOGGING_CONFIG)
    queue_handler = logging.getHandlerByName('queue_handler')
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

if __name__ == "__main__":
    verity_config = VerityConfig()
    logger = logging.getLogger(__name__)
    set_up_logging(verity_config)
    logger.info('app starting')
    verity = database(verity_config)
    verity.build_database()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = verity_config.SECRET_KEY
    app.register_blueprint(home_bp)

    app.run(debug=True)
