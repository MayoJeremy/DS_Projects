import os
import tkinter as tk
from pathlib import Path
from calculator.calculator import Calculator

os.chdir(Path(__file__).parent)

WINDOW = tk.Tk()


def main():
    Calculator(WINDOW)
    WINDOW.mainloop()


if __name__ == "__main__":
    main()
