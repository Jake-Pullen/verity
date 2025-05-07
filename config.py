import os
import yaml

class VerityConfig:

    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secure_secret_key'
        self.DATABASE = 'Verity.db'
        self.CONFIG_FILE_DIRECTORY = 'config_files'
        self.logging_config = self.load_config_file('logging_config.yaml')
        self.DATABASE_SCHEMA = self.load_config_file('verity_schema.yaml')

    def load_config_file(self, file):
        config = ''
        filepath = os.path.join(self.CONFIG_FILE_DIRECTORY,file)
        with open(filepath, 'r') as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        return config
