import tkinter as tk
import config as cfg
from calculator.calculator import Calculator
from calculator.cwindow import Cwindow


WINDOW = tk.Tk()


def main():
    c_ui = Cwindow(WINDOW)
    Calculator(c_ui)
    WINDOW.mainloop()


if __name__ == "__main__":
    main()
