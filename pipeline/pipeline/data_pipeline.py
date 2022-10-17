"""Providing functionality for a simple ETL-Pipeline

module consists of following functions:

"""
from pathlib import Path
from typing import Generator

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def extract_data(filename: str) -> Generator:
    """Read large data file.

    Args:
        filename (str): name of file

    Yields:
        File Iterator
    """
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def split_line(fg: Generator) -> Generator:
    """Split String to list.

    Args:
        fg (Generator): File Iterator

    Yields:
        Generator: File Iterator
    """
    for line in fg:
        yield line.split(",")


def remove_from_list(fg: Generator) -> Generator:
    """Remove first element from list.

    Args:
        fg (Generator): File Iterator

    Yields:
        Generator: File Iterator
    """
    for line in fg:
        line.pop(0)
        yield line


def load_data(filename: str):
    file_generator = extract_data(filename)
    split_generator = split_line(file_generator)
    remove_generator = remove_from_list(split_generator)


if __name__ == "__main__":
    load_data("techcrunch.csv")
