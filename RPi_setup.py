import os
import platform


def main():
    if platform.system() == "Windows":
        os.system("pip install RPi-1.0-py2.py3-none-any.whl")
    elif platform.system() == "Linux":
        os.system("pip3 install RPi-1.0-py2.py3-none-any.whl")
    else:
        print("This script hasn't been tested on your os, please install the package manually")


if __name__ == "__main__":
    main()
