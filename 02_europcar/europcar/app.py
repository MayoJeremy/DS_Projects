import os
import sqlite3
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
conn = sqlite3.connect("./data/europcar.db")
cursor = conn.cursor()


def main():
    pass


if __name__ == "__main__":
    main()

conn.close()
