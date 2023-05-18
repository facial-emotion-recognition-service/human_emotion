import os
from core.model import model
from human_emotion.core.predictors import get_face_emotions, get_image_emotions
import json

if __name__ == '__main__':
    model_path = os.environ.get("MODEL_PATH", "models/model.h5")
    config_path = os.environ.get("CONFIG_PATH", "config.json")

    with open(config_path, "r") as json_config_file:
        config_data = json.load(json_config_file)

    model_ = model(model_path, config_data)

    img_path = 'raw_data/faces/anger/2Q__ (1)_face.png'
    print(get_face_emotions(model_,img_path))
    #print(get_image_emotions(model_,img_path))
