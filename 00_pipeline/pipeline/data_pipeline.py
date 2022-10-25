"""Providing functionality for a simple ETL-Pipeline

module consists of following functions:

"""
from pathlib import Path
from typing import Callable, Generator

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def extract_data(filename: str) -> Generator:
    """Read large data file.

    Args:
        filename (str): name of file

    Yields:
        File Iterator
    """
    try:
        with open(DATA_DIR / filename, encoding="utf-8") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("Die Datei konnte nicht gefunden werden.")
        exit(-1)


def split_line(fg: Generator, seperator: str = ",") -> Generator:
    """Obsoluete. Split String to list.

    Args:
        fg (Generator): File Iterator

    Yields:
        Generator: File Iterator
    """
    for line in fg:
        if isinstance(line, str):
            yield line.split(seperator)


def split_closure(seperator: str = ",") -> Callable:
    def inner(fg: Generator) -> Generator:
        """Split String to list."""
        for line in fg:
            if isinstance(line, str):
                yield line.split(seperator)
    return inner


def remove_from_list(fg: Generator) -> Generator:
    """Remove first element from list.

    Args:
        fg (Generator): File Iterator

    Yields:
        Generator: File Iterator
    """
    for line in fg:
        try:
            line.pop(0)
            yield line
        except ValueError:
            pass


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


def load_data(filename: str) -> Generator:
    """Bessere Pipeline"""
    pipeline = [
        extract_data,
        split_closure(","),
        remove_from_list,
        filter_lines,
        dictify
    ]
    gen = filename
    for fn in pipeline:
        gen = fn(gen)
    return gen


def load_data_old(filename: str) -> Generator:
    file_generator = extract_data(filename)
    split_generator = split_line(file_generator)
    remove_generator = remove_from_list(split_generator)
    filter_generator = filter_lines(remove_generator)
    dict_generator = dictify(filter_generator)

    return dict_generator
    # result = next(dict_generator)
    # print(result)


if __name__ == "__main__":
    print(list(load_data("techcrunch.csv")))
