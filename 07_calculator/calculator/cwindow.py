import config as cfg
import tkinter as tk
from tkinter import ttk


class Cwindow:
    def __init__(self, window) -> None:
        self.window = window
        self.window.title(cfg.APP_TITLE)
        self.window.geometry(f"{cfg.APP_WIDTH}x{cfg.APP_HEIGHT}")
        self.window.config(bg="white")
        self.input_buttons_dict = {}
        self.label_text_dict = {}

    def add_input_button(
        self, btn_name: str, btn_row: int, btn_column: int, btn_span: int = 1
    ):
        self.input_buttons_dict[btn_name] = ttk.Button(
            self.window,
            text=btn_name,
            width=cfg.NUM_WIDTH,
            command=lambda: self.add_sym_to_input(btn_name),
        )
        self.input_buttons_dict[btn_name].grid(
            row=btn_row, column=btn_column, columnspan=btn_span
        )

    def bind_input_button(self, btn_name):
        self.window.bind(btn_name, lambda _: self.add_sym_to_input(btn_name))

    def add_bind_eq_button(self, btn_row: int, btn_column: int, btn_span: int = 1):
        ttk.Button(
            self.window,
            text="=",
            width=cfg.OPER_WIDTH * 2,
            command=self.calculate_and_display_result,
        ).grid(row=btn_row, column=btn_column, columnspan=btn_span)
        self.window.bind("<Return>", self.calculate_and_display_result)

    def add_bind_clear_button(self, btn_row: int, btn_column: int, btn_span: int = 1):
        ttk.Button(
            self.window,
            text="Del",
            width=cfg.OPER_WIDTH * 2,
            command=self.clear_input_label,
        ).grid(row=btn_row, column=btn_column, columnspan=btn_span)
        self.window.bind("<BackSpace>", self.clear_input_label)

    def add_label(self, lbl_name, lbl_row, lbl_column, lbl_span=1):
        self.label_text_dict[lbl_name] = tk.StringVar()
        ttk.Label(
            self.window,
            width=cfg.LABEL_WIDTH,
            textvariable=self.label_text_dict[lbl_name],
        ).grid(row=lbl_row, column=lbl_column, columnspan=lbl_span)

    def add_sym_to_input(self, symbol_to_add):
        self.label_text_dict["input_label"].set(
            self.label_text_dict["input_label"].get() + symbol_to_add
        )

    def clear_input_label(self, event=None):
        self.label_text_dict["input_label"].set("")

    def calculate_and_display_result(self, event=None):
        result = ""
        input_field = self.label_text_dict["input_label"].get()
        try:
            if input_field[0].isdigit():
                result = eval(input_field)  # careful, can insert pythoncode
            elif input_field:
                result = eval(self.label_text_dict["result_label"].get() + input_field)
        except IndexError:
            return
        except SyntaxError:
            input_field = input_field.lstrip("0")
            self.label_text_dict["input_label"].set(input_field)
        else:
            self.label_text_dict["result_label"].set(result)
            self.clear_input_label()
