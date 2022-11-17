import config as cfg
import tkinter as tk


class Calculator:
    def __init__(self, window) -> None:
        self.window = window
        self.setup_gui()

    def setup_gui(self):
        self.window.title(cfg.APP_TITLE)
        self.window.geometry(f"{cfg.APP_WIDTH}x{cfg.APP_HEIGHT}")
        self.result_label()
        self.input_label()
        self.create_numpad()
        self.create_operand_selection()

    def result_label(self):
        tk.Label(self.window, text="Result label").grid(row=0, column=0, columnspan=3)

    def input_label(self):
        tk.Label(self.window, text="Input label").grid(row=1, column=0, columnspan=3)

    def create_numpad(self):
        def add_sym(number_to_add):
            print(number_to_add)

        tk.Button(self.window, text="1", command=lambda: add_sym("1")).grid(
            row=2, column=0
        )
        tk.Button(self.window, text="2", command=lambda: add_sym("2")).grid(
            row=2, column=1
        )
        tk.Button(self.window, text="3", command=lambda: add_sym("3")).grid(
            row=2, column=2
        )
        tk.Button(self.window, text="4", command=lambda: add_sym("4")).grid(
            row=3, column=0
        )
        tk.Button(self.window, text="5", command=lambda: add_sym("5")).grid(
            row=3, column=1
        )
        tk.Button(self.window, text="6", command=lambda: add_sym("6")).grid(
            row=3, column=2
        )
        tk.Button(self.window, text="7", command=lambda: add_sym("7")).grid(
            row=4, column=0
        )
        tk.Button(self.window, text="8", command=lambda: add_sym("8")).grid(
            row=4, column=1
        )
        tk.Button(self.window, text="9", command=lambda: add_sym("9")).grid(
            row=4, column=2
        )
        tk.Button(self.window, text="0", command=lambda: add_sym("0")).grid(
            row=5, column=0, columnspan=3
        )

    def create_operand_selection(self):
        tk.Button(self.window, text="+").grid(row=2, column=3)
        tk.Button(self.window, text="-").grid(row=3, column=3)
        tk.Button(self.window, text="*").grid(row=4, column=3)
        tk.Button(self.window, text="/").grid(row=5, column=3)
        tk.Button(self.window, text="=").grid(row=6, column=3)
