import tkinter as tk
import config as cfg
from calculator.calculator import Calculator


WINDOW = tk.Tk()


def main():
    Calculator(WINDOW)
    WINDOW.mainloop()


if __name__ == "__main__":
    main()
