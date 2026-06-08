from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    author="nhantranng-bit",
    description="An emotion detection application package using Watson NLP",
    install_requires=[
        "requests",
    ],
)
