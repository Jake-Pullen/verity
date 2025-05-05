import os
import logging
import logging.config
import atexit
import yaml

from flask import Flask

from data_handler import database

def set_up_logging():
    with open('config/logging_config.yaml', 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
    logging.config.dictConfig(config)
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
    os.makedirs('logs', exist_ok=True)
    set_up_logging()
    logger.info('app started')
    verity = database()
    verity.check_database_exists()
    app.run(debug=True)
