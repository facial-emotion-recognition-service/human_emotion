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
        print(
            list(map(lambda x: model.label_dict_num2text[x], preds_sorted_indices))[
                : top_n
            ]
        )
    elif ret == "num":
        print(preds_sorted_indices[: top_n])


    pass
