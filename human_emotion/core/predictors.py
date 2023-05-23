import human_emotion.core.extraction as extraction
from human_emotion.core.model import Model


class Predictor:
    def __init__(self, model_path, config_data):
        self.model = Model(model_path, config_data)

    def get_face_image_emotions(self, face_image_file, top_n=1, ret="text"):
        """Returns the top n emotions for an image of a single, isolated face.

        Retrieves the top n emotions from an image of a single, isolated face,
        along with their probabilities.

        Args:
            face_image_file: Path to the face image file.
            top_n: Number of top emotions to return.
            ret: Label type for the returned dict. One of "text" or "num".

        Returns:
            A dict mapping the top n emotions to their probabilities.
        """
        img_array = self.model.preprocess_file(face_image_file)
        result = self._get_face_emotions(img_array, top_n, ret)

        return result

    # TODO(https://trello.com/c/p9RyBsxE): Refactor once extraction is done.
    # This is an "internal" (private, or rather: protected) method put in place
    # only for compatibility with Nathan's WiP on extraction. To be refactored
    # and merged with get_face_image_emotions().

    def _get_face_emotions(self, face, top_n=1, ret="text"):
        predictions = self.model.predict(face)[0]
        preds_sorted = sorted(predictions, reverse=True)
        preds_sorted_indices = [
            i
            for i, _ in sorted(
                enumerate(predictions), key=lambda x: x[1], reverse=True
            )
        ]
        top_n_preds_num = preds_sorted_indices[:top_n]
        top_n_preds_text = list(
            map(lambda x: self.model.labels_num2text[x], top_n_preds_num)
        )
        dict_labels = top_n_preds_text if ret == "text" else top_n_preds_num
        result = {
            label: float(preds_sorted[i]) for i, label in enumerate(dict_labels)
        }

        return result

    def get_image_emotions(self, image_file, top_n=1, ret="text"):
        """Returns the top n emotions for all deteceted faces in an image.

        Retrieves the top n emotions for each face detected in an image file,
        along with their probabilities and the coordinates of the face.

        Args:
            image_file: Path to the image file.
            top_n: Number of top emotions to return.
            ret: Label type for the returned dict. One of "text" or "num".

        Returns:
            A list of dictionaries with each element containing a "prediction"
            and a "coords" item. The former is a dict mapping the top n emotions
            to their probabilities and the latter contains the coordinates of
            the face. An empty list is returned if no faces are detected.
        """
        face_emotions = []

        face_coords, image = extraction.extract_faces(image_file)
        for x1, x2, y1, y2 in face_coords:
            face = image[x1:x2, y1:y2]
            face_preprocessed = self.model.preprocess(face)
            predictions = self.get_face_emotions(face_preprocessed, top_n, ret)
            face_emotions.append(
                {"prediction": predictions, "coords": (x1, x2, y1, y2)}
            )

        return face_emotions
