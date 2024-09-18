from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BotSync",
    version="0.1.0",
    description=long_description,
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "torch>=1.9.0",
        "torchvision>=0.10.0",
    ],
    include_package_data=True,  # Include data files specified in package_data
)