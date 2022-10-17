"""
Hauptprogramm
"""

from data_pipeline import load_data


def main():
    for entry in load_data("techcrunch.csv"):
        print(entry)


if __name__ == "__main__":
    main()
