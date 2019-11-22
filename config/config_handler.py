import json


class ConfigHandler():
    def __init__(self, config_path):
        self.config_path = config_path
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def api(self):
        return self.config['api']

    def request(self):
        return self.config['request']

    def languages(self):
        return self.config['languages']

    def db_relative_path(self):
        return self.config['db_relative_path']


config = ConfigHandler("../config/config.json")
