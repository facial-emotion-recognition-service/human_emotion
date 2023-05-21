import json


class ModelConfigProvider:
    def __init__(self, config_path):
        self._config_data = {}
        with open(config_path, "r") as json_config_file:
            self._config_data = json.load(json_config_file)

    @property
    def config_data(self):
        return self._config_data
