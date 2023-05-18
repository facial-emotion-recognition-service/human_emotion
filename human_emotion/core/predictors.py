import human_emotion.core.extraction as extraction

def get_face_emotions(model, face_image, top_n = 1, ret = 'text'):
    '''Returns a list of tuples for the top N emotions of a single face that is
    already isolated (but not the correct size)
    See get_face_emotions for function of top_n and ret parameters.'''
    img = model.preprocess(face_image)
    predictions = model.predict(img)
    preds_sorted_indices = [
        i for i, _ in sorted(enumerate(predictions), key=lambda x: x[1], reverse=True)
    ]
    if ret == "text":
        return {'prediction': (
        list(map(lambda x: model.label_dict_num2text[x], preds_sorted_indices))[
            : top_n
        ]
    )}
    elif ret == "num":
        return {'prediction': preds_sorted_indices[: top_n]}

def get_image_emotions(model, image, top_n = 1, ret = 'text'):
    '''Returns a list of dicts containing  the top N emotions for all faces in an image.
    Also contains the the coords for each face.
    The first value of the tuple is an int or string. Defined by the ret parameter.
    If ret = text, the string will be the emotion (eg “happy”)
    If ret = num, the ,mapping between int and emotion can be gotten from the results of get_emo_map'''
    face_emotions = []

    face_coords, image = extraction.extract_faces(image)
    if face_coords:
        for x1, x2, y1, y2 in face_coords:
            face_img = image[x1: x2, y1:y2]
            face_img = model.preprocess(face_img)
            predictions = get_face_emotions(model, face_img, top_n, ret)
            face_emotions.append({'prediction': predictions, 'coords': (x1, x2, y1, y2)})

        return face_emotions
    return 'No faces detected'
