import platform
import sys


def main() -> int:
    if platform.system() == "Windows":
        print("windows code only specific")

    if platform.system() == "Linux":
        print("linux code only specific")

    print("Hello, world!")
    return 0
