import os
from human_emotion.core.predictors import Predictor
import json

if __name__ == "__main__":
    model_path = os.environ.get("MODEL_PATH", "models/model.h5")
    config_path = os.environ.get("CONFIG_PATH", "config.json")

    with open(config_path, "r") as json_config_file:
        config_data = json.load(json_config_file)

    predictor = Predictor(model_path, config_data)

    img_path = "../input_images/8_hap.png"
    print(predictor.get_face_image_emotions(img_path))
    # print(predictor.get_image_emotions(img_path))
