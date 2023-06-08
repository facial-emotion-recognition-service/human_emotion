import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from app_config_provider import AppConfigProvider
from model_config_provider import ModelConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY="4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh",
    IGNORABLE_404_URLS=[r"^favicon\.ico$"],
    ROOT_URLCONF=sys.modules[__name__],
)


def getHello(request):
    return HttpResponse("<h1>Hello from server!</h1>")


def getEmotionsFromImage(request, face_image_file):
    print("Server.getEmotionsFromImage.name = " + face_image_file)
    app.get_face_emotions_from_file(face_image_file, 8, "text")
    return HttpResponse("getEmotionsFromImage " + face_image_file)


urlpatterns = [
    path(r"hello", getHello),
    path(r"emotions/<face_image_file>", getEmotionsFromImage, name="some-name"),
]

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    model_config_path = app_config["config_path"]
    modelConfigProvider = ModelConfigProvider(model_config_path)
    argsProvider = ArgsProvider()

    config_path = app_config["config_path"]
    model_path = app_config["model_path"]
    image_input_dir = app_config["image_input_dir"]
    json_output_dir = app_config["json_output_dir"]

    model_config = modelConfigProvider.config_data

    app = AppLogic(model_path, image_input_dir, json_output_dir, model_config)

    execute_from_command_line(sys.argv)
