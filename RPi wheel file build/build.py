from setuptools import setup

setup(
    name='RPi',
    version='1.0',
    packages=['RPi', 'RPi/GPIO'],
    package_data={'': ['RPi/_GPIO.cpython-37m-arm-linux-gnueabihf.so']},
    include_package_data=True,
    install_requires=[],
    author="Rylan Meilutis",
    description="Allows for development of a program that uses gpio on a platform that doesn't have gpio."
)