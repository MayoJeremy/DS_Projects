import config as cfg
import tkinter as tk


class Calculator:
    def __init__(self, window) -> None:
        self.window = window
        self.input_string = tk.StringVar()
        self.setup_gui()

    def setup_gui(self):
        self.window.title(cfg.APP_TITLE)
        self.window.geometry(f"{cfg.APP_WIDTH}x{cfg.APP_HEIGHT}")
        self.result_label()
        self.input_label()
        self.create_numpad()
        self.create_operand_selection()

    def result_label(self):
        self.label_result = tk.Label(self.window, text="Result label")
        self.label_result.grid(row=0, column=0, columnspan=3)

    def input_label(self):
        self.label_input = tk.Label(self.window, textvariable=self.input_string)
        self.label_input.grid(row=1, column=0, columnspan=3)

    def add_sym_to_input(self, symbol_to_add):
        self.input_string.set(self.input_string.get() + symbol_to_add)

    def calculate_and_display_result(self):
        result = eval(self.input_string.get())  # careful, can insert pythoncode
        self.label_result.config(text=result)

    def clear_input_label(self):
        self.input_string.set("")

    def create_numpad(self):
        tk.Button(
            self.window,
            text="1",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("1"),
        ).grid(row=2, column=0)
        tk.Button(
            self.window,
            text="2",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("2"),
        ).grid(row=2, column=1)
        tk.Button(
            self.window,
            text="3",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("3"),
        ).grid(row=2, column=2)
        tk.Button(
            self.window,
            text="4",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("4"),
        ).grid(row=3, column=0)
        tk.Button(
            self.window,
            text="5",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("5"),
        ).grid(row=3, column=1)
        tk.Button(
            self.window,
            text="6",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("6"),
        ).grid(row=3, column=2)
        tk.Button(
            self.window,
            text="7",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("7"),
        ).grid(row=4, column=0)
        tk.Button(
            self.window,
            text="8",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("8"),
        ).grid(row=4, column=1)
        tk.Button(
            self.window,
            text="9",
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input("9"),
        ).grid(row=4, column=2)
        tk.Button(
            self.window,
            text="0",
            width=cfg.NUM_WIDTH * 3,
            command=lambda: self.add_sym_to_input("0"),
        ).grid(row=5, column=0, columnspan=3)

    def create_operand_selection(self):
        tk.Button(
            self.window,
            text="+",
            width=cfg.OPER_WIDTH,
            command=lambda: self.add_sym_to_input("+"),
        ).grid(row=2, column=3)
        tk.Button(
            self.window,
            text="-",
            width=cfg.OPER_WIDTH,
            command=lambda: self.add_sym_to_input("-"),
        ).grid(row=3, column=3)
        tk.Button(
            self.window,
            text="*",
            width=cfg.OPER_WIDTH,
            command=lambda: self.add_sym_to_input("*"),
        ).grid(row=4, column=3)
        tk.Button(
            self.window,
            text="/",
            width=cfg.OPER_WIDTH,
            command=lambda: self.add_sym_to_input("/"),
        ).grid(row=5, column=3)
        tk.Button(
            self.window,
            text="=",
            width=cfg.OPER_WIDTH * 2,
            command=self.calculate_and_display_result,
        ).grid(row=6, column=2, columnspan=2)
        tk.Button(
            self.window,
            text="Del",
            width=cfg.OPER_WIDTH * 2,
            command=self.clear_input_label,
        ).grid(row=6, column=0, columnspan=2)
