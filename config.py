import os
import yaml

class VerityConfig:

    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secure_secret_key'
        self.logging_config = self.load_logging_config()
        self.DATABASE = 'Verity.db'
        self.CONFIG_FILE_DIRECTORY = 'config_files'

    def load_config_file(self, file):
        logging_config = ''
        with open('config_files/logging_config.yaml', 'r') as f:
            try:
                logging_config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        return logging_config
