FROM python:3.10-buster

WORKDIR /emosense

RUN apt-get -y update && apt-get install -y build-essential cmake

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir output_json
COPY human_emotion .
# COPY config.json .

EXPOSE 8000

WORKDIR /emosense/interface
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
