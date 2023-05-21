import argparse


class ArgsProvider:
    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser()
        # Define command-line arguments and options using argparse
        parser.add_argument(
            "--face_image_file",
            type=str,
            help="full file name of a file containing an isolated image of a face",
        )
        parser.add_argument(
            "--top_n",
            default=1,
            type=int,
            help="maximum number of emotions to return per face",
        )
        parser.add_argument(
            "--ret",
            default="text",
            type=str,
            choices=["text", "num"],
            help="whether to return emotion labels as text ('text') or numbers ('num')",
        )
        args = parser.parse_args()
        return args
