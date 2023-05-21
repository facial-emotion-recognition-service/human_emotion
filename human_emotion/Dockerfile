FROM ubuntu

RUN apt-get update
RUN apt-get install -y python-is-python3
RUN apt-get install -y python3-pip

ADD interface /interface
WORKDIR /interface
EXPOSE 8000

#python manage.py runserver 0.0.0.0:8000
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]

