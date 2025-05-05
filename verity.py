import os
import logging
import logging.config
import atexit

from flask import Flask

from data_handler import database
from config import VerityConfig

def set_up_logging(config):
    logging.config.dictConfig(config.logging_config)
    queue_handler = logging.getHandlerByName('queue_handler')
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.debug('hello world page load')
    return '<h1>Hello World</h1>'

if __name__ == "__main__":
    config = VerityConfig()
    os.makedirs('logs', exist_ok=True)
    set_up_logging(config)
    logger.info('app started')
    verity = database(config)
    verity.build_database()
    app.run(debug=True)
