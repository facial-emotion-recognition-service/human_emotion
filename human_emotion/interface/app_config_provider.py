import os


class AppConfigProvider:
    def __init__(self):
        self._model_path = os.environ.get("MODEL_PATH", "../models/model.h5")
        self._config_path = os.environ.get("CONFIG_PATH", "../config.json")
        self._image_input_dir = os.environ.get("IMAGE_INPUT_DIR")
        self._json_output_dir = os.environ.get("JSON_OUTPUT_DIR")

    @property
    def app_config(self):
        result = {
            "model_path": self._model_path,
            "config_path": self._config_path,
            "image_input_dir": self._image_input_dir,
            "json_output_dir": self._json_output_dir,
        }

        return result
