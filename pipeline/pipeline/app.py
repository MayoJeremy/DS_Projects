"""
Hauptprogramm
"""

from data_pipeline import load_data


def main():
    load_data("techcrunch.csv")


if __name__ == "__main__":
    main()
