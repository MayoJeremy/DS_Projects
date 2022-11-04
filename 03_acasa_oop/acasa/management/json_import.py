import json
import os
from pathlib import Path


os.chdir(Path(__file__).parent.parent.parent)


class JsonImporter:
    def __init__(self, file: str) -> None:
        """

        Args:
            file (str): Path + Filename to import
        """
        self.file = "./data/" + file  # "./data/menu.json"

    def get_content(self):
        """loads Jsonfile into instance based variable 'menu'"""
        with open(self.file, mode="r", encoding="UTF-8") as file_in:
            self.menu = json.load(file_in)


def main():
    js1 = JsonImporter()
    js1.get_content()
    print(js1.menu)


if __name__ == "__main__":
    main()
