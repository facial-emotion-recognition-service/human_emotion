import argparse


class ConsoleApp:
    def __init__(self, args):
        # Initialize any necessary variables and objects based on command-line arguments
        pass

    def run(self):
        # Main program logic goes here
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Define command-line arguments and options using argparse
    parser.add_argument(
        "--face_image_path", type=str, help="path to a file containing an isolated image of a face"
    )
    parser.add_argument(
        "--top_n", default=1, type=int, help="maximum number of emotions to return per face"
    )
    parser.add_argument(
        "--ret",
        default="text",
        type=str,
        choices=["text", "num"],
        help="whether to return emotion labels as text ('text') or numbers ('num')",
    )
    args = parser.parse_args()

    app = ConsoleApp(args)
    app.run()
