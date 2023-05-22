FROM python:3.10-buster

WORKDIR /emosense

RUN apt-get -y update && apt-get install -y build-essential cmake

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir output_json
COPY human_emotion .
COPY config.json .
COPY input_images/ input_images/
COPY models/ models/

ENV MODEL_PATH="../models/model.h5"
ENV CONFIG_PATH="../config.json"
ENV IMAGE_INPUT_DIR="../input_images/"
ENV JSON_OUTPUT_DIR="../output_json/"

EXPOSE 8000

WORKDIR /emosense/interface
#python manage.py runserver 0.0.0.0:8000
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
