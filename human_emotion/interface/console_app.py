import argparse
import os
import numpy as np
import tensorflow as tf


class ConsoleApp:
    def __init__(self, model_path):
        # Initialize any necessary variables and objects based on command-line arguments
        self.model = tf.keras.models.load_model(model_path, compile=True)

    def run(self, args):
        # Main program logic goes here
        if args.face_image_path:
            img = tf.keras.preprocessing.image.load_img(
                args.face_image_path, target_size=(224, 224)
            )
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
            print(self.model.predict(img_array))


if __name__ == "__main__":
    model_path = os.environ.get("MODEL_PATH", "../models/model.h5")

    parser = argparse.ArgumentParser()
    # Define command-line arguments and options using argparse
    parser.add_argument(
        "--face_image_path", type=str, help="path to a file containing an isolated image of a face"
    )
    parser.add_argument(
        "--top_n", default=1, type=int, help="maximum number of emotions to return per face"
    )
    parser.add_argument(
        "--ret",
        default="text",
        type=str,
        choices=["text", "num"],
        help="whether to return emotion labels as text ('text') or numbers ('num')",
    )
    args = parser.parse_args()

    app = ConsoleApp(model_path)
    app.run(args)
