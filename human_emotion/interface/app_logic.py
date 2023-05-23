import json
import pathlib
import numpy as np
import tensorflow as tf


class AppLogic:
    def __init__(
        self, model_path, image_input_dir, json_output_dir, config_data
    ):
        self.model = tf.keras.models.load_model(model_path, compile=True)

        self.image_input_dir = pathlib.Path(image_input_dir)
        self.json_output_dir = pathlib.Path(json_output_dir)

        self.labels_text2num = config_data["labels_text2num"]
        self.labels_num2text = {v: k for k, v in self.labels_text2num.items()}

    def get_face_emotions(self, face_image_name, top_n, ret):
        img_path = pathlib.Path(self.image_input_dir, face_image_name)
        img = tf.keras.preprocessing.image.load_img(
            img_path, target_size=(224, 224)
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
        predictions = self.model.predict(img_array)[0]
        preds_sorted = sorted(predictions, reverse=True)
        preds_sorted_indices = [
            i
            for i, _ in sorted(
                enumerate(predictions), key=lambda x: x[1], reverse=True
            )
        ]
        top_n_preds_num = preds_sorted_indices[:top_n]
        top_n_preds_text = list(
            map(lambda x: self.labels_num2text[x], top_n_preds_num)
        )
        dict_labels = top_n_preds_text if ret == "text" else top_n_preds_num
        result = {}
        for i, label in enumerate(dict_labels):
            result[label] = float(preds_sorted[i])

        print(result)

        json_str = json.dumps(result, indent=4)
        json_filename = img_path.stem + ".json"
        json_file_path = pathlib.Path(self.json_output_dir, json_filename)
        with open(json_file_path, "w") as f:
            f.write(json_str)
