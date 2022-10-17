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


def filter_lines(fg: Generator) -> Generator:
    """Filter entries by State (CA)

    Args:
        fg (Generator): File Iterator

    Yields:
        Generator: File Iterator
    """
    return (line for line in fg if line[4] in ["CA", "state"])


def dictify(fg: Generator) -> Generator:
    """Create Dict for each entry.

    Args:
        fg (Generator): file iterator

    Yields:
        Generator: file iterator
    """
    header = next(fg)
    return (dict(zip(header, line)) for line in fg)


def load_data(filename: str):
    file_generator = extract_data(filename)
    split_generator = split_line(file_generator)
    remove_generator = remove_from_list(split_generator)
    filter_generator = filter_lines(remove_generator)
    dict_generator = dictify(filter_generator)
    # result = next(dict_generator)
    # print(result)


if __name__ == "__main__":
    load_data("techcrunch.csv")
