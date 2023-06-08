# 1 Project Outline
This is a project to:
- use deep learning techniques to train a model on images of isolated human faces and recognize the emotion expressed therein
- use image segmentation techniques to isolate faces in _any_ image and perform the abovementioned classification task on each face
- provide an interface (a console app, an API, and/or a web UI) to be able to use the trained model for inference on any custom image

# 2 Project Structure
**Note:** This repo may be split in the future to house various components of the proeject separately. This document will be updated accordingly. The project is work in progress, but we will strive to keep this document current.

## 2.1 The Model
Currently, model training is performed independently in the Jupyter notebooks under the `notebooks` folder. The model was trained on Google Colab with a GPU back-end. The resulting file containing the trained weights ("the model file") is not uploaded to the code repo as it can get fairly large in size.

## 2.2 The App

### 2.2.1 The Console App
At this point, the console app is only able to predict emotions from a PNG image of a single, isolated face. (**Note:** We use the words "infer" and "predict" interchangeably throughout this document).

#### Instructions on how to install:
1. Install python 3.10
2. Clone this repo
3. `cd` into the projet directory and `pip install -r requirements.txt`
4. `mkdir models` and copy the model file (named `model.h5`) into the newly-created folder.  
Alternatively, name the file _anything_ and put it in _any_ folder, but:
```
export MODEL_PATH="full path to the model file"
```
5. `mkdir input_images` in the project's root folder and put the PNG image(s) you'd like to run inference on in the newly-created folder.  
Alternatively, put the image(s) in _any_ folder, but:
```
export IMAGE_INPUT_DIR="path to folder containing PNG image(s)"
```
6. `mkdir output_json` in the project's root folder.  
Alternatively, name this folder _anything_, but:
```
export JSON_OUTPUT_DIR="path to folder where you want JSON files stored"
```

#### Instructions on how to run inference:
1. While in the project's root directory `cd human_emotion/interface` (change the `/` to `\` on Windows).
2. Run the following command to get help on how to use the console app:
```
python main_console.py --help
```
**Example:** `python main_console.py --face_image_file "sample_image.png" --ret text --top_n 3` will return the top 3 predicted emotions for the specified image, along with their corresponding probabilities, with the emotion labels presented as text (e.g. "happiness")

The results are printed out to the console and also written to a JSON file with the same name as the image file. (The file will be overwritten if it already exists).
