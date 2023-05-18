import tensorflow as tf
import numpy as np

class model:
    def __init__(self, model_path, config_data):
        self.model = tf.keras.models.load_model(model_path, compile=True)
        self.label_dict_text2num = config_data["label_dict_text2num"]
        self.label_dict_num2text = {}
        for key, value in self.label_dict_text2num.items():
            self.label_dict_num2text[value] = key

    @staticmethod
    def preprocess(face_image):
        if isinstance(face_image, str):
            img = tf.keras.preprocessing.image.load_img(
            face_image, target_size=(224, 224)
        )
            img_array = tf.keras.preprocessing.image.img_to_array(img)
        else:
            img_array = face_image
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.vgg16.preprocess_input(img_array)

        return img_array

    def predict(self, img_array):
        return self.model.predict(img_array)
