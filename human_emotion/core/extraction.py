import cv2 as cv
import face_recognition
import os

## TO DO: Store in config file
IMAGES = ['.png','.jpg']
VIDEOS = ['.mp4']

dir_ = '/home/nathan/code/nihonlanguageprocessing/human_emotion/raw_data/faces_extraction'
im_file = 'image1.jpg'
path = os.path.join(dir_,im_file)

faces = []

def get_type(path: str) -> str:
    _, ext = os.path.splitext(path)
    if ext in IMAGES:
        return 'img'
    elif ext in VIDEOS:
        return 'vid'
    return None


def extract_faces(path):
    type_ = get_type(path)

    if type_ == 'img':
        img = cv.imread(path)
    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(BGRtoRGB(img))
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv.rectangle(img, (left, top), (right, bottom), (0, 0,
        255), 2)
    # Display the resulting image
    cv.imshow('Image', img)
    cv.imwrite('/home/nathan/code/nihonlanguageprocessing/human_emotion/raw_data/faces_extraction/extracted1.jpg', img)
    cv.waitKey(0)

def BGRtoRGB(img):

    return img[:, :, ::-1]

if __name__ == '__main__':
    extract_faces(path)
