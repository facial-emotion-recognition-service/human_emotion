import json
from pathlib import Path
from human_emotion.core.predictors import Predictor


class AppLogic:
    def __init__(
        self, model_path, image_input_dir, json_output_dir, config_data
    ):
        self.predictor = Predictor(model_path, config_data)

        self.image_input_dir = Path(image_input_dir)
        self.json_output_dir = Path(json_output_dir)

    def get_face_emotions_from_file(self, face_image_name, top_n, ret):
        img_path = Path(self.image_input_dir, face_image_name)
        result = self.predictor.get_face_image_emotions(img_path, top_n, ret)
        print(result)

        json_str = json.dumps(result, indent=4)
        json_filename = img_path.stem + ".json"
        json_file_path = Path(self.json_output_dir, json_filename)
        with open(json_file_path, "w") as f:
            f.write(json_str)
