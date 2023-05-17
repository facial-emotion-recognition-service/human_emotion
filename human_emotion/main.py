import os
from core.model import model
import json

if __name__ == '__main__':
    model_path = os.environ.get("MODEL_PATH", "../models/model.h5")
    config_path = os.environ.get("CONFIG_PATH", "../config.json")

    with open(config_path, "r") as json_config_file:
        config_data = json.load(json_config_file)

    model_ = model(model_path, config_data)
