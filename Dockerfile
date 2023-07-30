FROM python:3.10-buster

ADD human_emotion ./human_emotion

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip
RUN pip install .

WORKDIR /human_emotion
ADD models ./models
RUN mkdir input_images
RUN mkdir output_json
COPY config.json .

EXPOSE 8000

WORKDIR /human_emotion/interface
ENV IMAGE_INPUT_DIR="../input_images/"
ENV JSON_OUTPUT_DIR="../output_json/"
ENV MODEL_PATH="../models/model.h5"
ENV CONFIG_PATH="../config.json"

CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
