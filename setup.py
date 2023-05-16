from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="human_emotion",
    # version="0.0.1",
    description="Human Emotion Recognition",
    # license="MIT",
    # author="",
    # author_email="",
    # url="",
    install_requires=requirements,
    packages=find_packages(),
    # scripts=['human_emotion/scripts/test_script.py'],
    test_suite="tests",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    # zip_safe=False,
)
