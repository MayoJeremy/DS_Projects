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
