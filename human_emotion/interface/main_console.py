from app_config_provider import AppConfigProvider
from model_config_provider import ModelConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

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
    args = argsProvider.getArgs()

    app = AppLogic(model_path, image_input_dir, json_output_dir, model_config)
    app.get_face_emotions_from_file(args.face_image_file, args.top_n, args.ret)
