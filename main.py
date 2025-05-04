import os
import logging

from flask import Flask
from logging.handlers import RotatingFileHandler

from data_handler import database

def configure_logging():
    # Configure logger with rotating file handler and custom log levels
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] %(name)s.%(funcName)s: %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotate logs every 10 MB, keeping 5 backups
    file_handler = RotatingFileHandler('logs/verity.log', maxBytes=1024*1024*10, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.debug('hello world page load')
    return '<p>Hello World</p>'

if __name__ == "__main__":
    os.makedirs('logs', exist_ok=True)
    logger = configure_logging()
    verity = database()
    verity.check_database_exists()
    app.run(debug=True)
