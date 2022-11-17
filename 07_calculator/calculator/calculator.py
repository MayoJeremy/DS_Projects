import config as cfg
import tkinter as tk


class Calculator:
    def __init__(self, window) -> None:
        self.window = window
        self.input_string = tk.StringVar()
        self.result_string = tk.StringVar()
        self.setup_gui()

    def setup_gui(self):
        self.window.title(cfg.APP_TITLE)
        self.window.geometry(f"{cfg.APP_WIDTH}x{cfg.APP_HEIGHT}")
        self.window.config(bg="white")
        self.result_label()
        self.input_label()
        self.create_numpad()
        self.create_operand_selection()
        self.bind_numbers_to_window()
        self.bind_operations_to_window()

    def bind_numbers_to_window(self):
        self.window.bind("1", lambda ev: self.add_sym_to_input("1"))
        self.window.bind("2", lambda ev: self.add_sym_to_input("2"))
        self.window.bind("3", lambda ev: self.add_sym_to_input("3"))
        self.window.bind("4", lambda ev: self.add_sym_to_input("4"))
        self.window.bind("5", lambda ev: self.add_sym_to_input("5"))
        self.window.bind("6", lambda ev: self.add_sym_to_input("6"))
        self.window.bind("7", lambda ev: self.add_sym_to_input("7"))
        self.window.bind("8", lambda ev: self.add_sym_to_input("8"))
        self.window.bind("9", lambda ev: self.add_sym_to_input("9"))
        self.window.bind("0", lambda ev: self.add_sym_to_input("0"))

    def bind_operations_to_window(self):
        self.window.bind("+", lambda ev: self.add_sym_to_input("+"))
        self.window.bind("-", lambda ev: self.add_sym_to_input("-"))
        self.window.bind("*", lambda ev: self.add_sym_to_input("*"))
        self.window.bind("/", lambda ev: self.add_sym_to_input("/"))
        self.window.bind("<BackSpace>", self.clear_input_label)
        self.window.bind("<Return>", self.calculate_and_display_result)

    def result_label(self):
        self.label_result = tk.Label(
            self.window,
            width=cfg.LABEL_WIDTH,
            height=cfg.LABEL_HEIGHT,
            bg="grey",
            textvariable=self.result_string,
        )
        self.label_result.grid(row=0, column=0, columnspan=3)

    def input_label(self):
        self.label_input = tk.Label(
            self.window,
            width=cfg.LABEL_WIDTH,
            height=cfg.LABEL_HEIGHT,
            textvariable=self.input_string,
        )
        self.label_input.grid(row=1, column=0, columnspan=3)

    def add_sym_to_input(self, symbol_to_add):
        self.input_string.set(self.input_string.get() + symbol_to_add)

    def calculate_and_display_result(self, event=None):
        result = eval(self.input_string.get())  # careful, can insert pythoncode
        self.result_string.set(result)


    def clear_input_label(self, event=None):
        self.input_string.set("")

    def create_numpad(self):
        tk.Button(
            self.window,
            text="1",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("1"),
        ).grid(row=2, column=0)
        tk.Button(
            self.window,
            text="2",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("2"),
        ).grid(row=2, column=1)
        tk.Button(
            self.window,
            text="3",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("3"),
        ).grid(row=2, column=2)
        tk.Button(
            self.window,
            text="4",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("4"),
        ).grid(row=3, column=0)
        tk.Button(
            self.window,
            text="5",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("5"),
        ).grid(row=3, column=1)
        tk.Button(
            self.window,
            text="6",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("6"),
        ).grid(row=3, column=2)
        tk.Button(
            self.window,
            text="7",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("7"),
        ).grid(row=4, column=0)
        tk.Button(
            self.window,
            text="8",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("8"),
        ).grid(row=4, column=1)
        tk.Button(
            self.window,
            text="9",
            width=cfg.NUM_WIDTH,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("9"),
        ).grid(row=4, column=2)
        tk.Button(
            self.window,
            text="0",
            width=cfg.NUM_WIDTH * 3,
            height=cfg.NUM_HEIGHT,
            command=lambda: self.add_sym_to_input("0"),
        ).grid(row=5, column=0, columnspan=3)

    def create_operand_selection(self):
        tk.Button(
            self.window,
            text="+",
            width=cfg.OPER_WIDTH,
            height=cfg.OPER_HEIGHT,
            command=lambda: self.add_sym_to_input("+"),
        ).grid(row=2, column=3)
        tk.Button(
            self.window,
            text="-",
            width=cfg.OPER_WIDTH,
            height=cfg.OPER_HEIGHT,
            command=lambda: self.add_sym_to_input("-"),
        ).grid(row=3, column=3)
        tk.Button(
            self.window,
            text="*",
            width=cfg.OPER_WIDTH,
            height=cfg.OPER_HEIGHT,
            command=lambda: self.add_sym_to_input("*"),
        ).grid(row=4, column=3)
        tk.Button(
            self.window,
            text="/",
            width=cfg.OPER_WIDTH,
            height=cfg.OPER_HEIGHT,
            command=lambda: self.add_sym_to_input("/"),
        ).grid(row=5, column=3)
        tk.Button(
            self.window,
            text="=",
            width=cfg.OPER_WIDTH * 2,
            height=cfg.OPER_HEIGHT,
            command=self.calculate_and_display_result,
        ).grid(row=6, column=2, columnspan=2)
        tk.Button(
            self.window,
            text="Del",
            width=cfg.OPER_WIDTH * 2,
            height=cfg.OPER_HEIGHT,
            command=self.clear_input_label,
        ).grid(row=6, column=0, columnspan=2)
