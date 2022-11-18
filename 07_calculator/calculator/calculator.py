import config as cfg
from calculator.cwindow import Cwindow


class Calculator:
    def __init__(self, ui: Cwindow) -> None:
        self.ui = ui
        self.setup_gui()

    def setup_gui(self):
        self.result_label()
        self.input_label()
        self.create_numpad()
        self.create_operand_selection()

    def result_label(self):
        self.ui.add_label("result_label", 0, 0, 3)

    def input_label(self):
        self.ui.add_label("input_label", 1, 0, 3)

    def create_numpad(self):
        for sym, values in cfg.NUMBERS_AVAILABLE.items():
            self.ui.add_input_button(sym, *values)
            self.ui.bind_input_button(sym)

    def create_operand_selection(self):
        for ope, val in cfg.OPERANT_AVAILABLE.items():
            self.ui.add_input_button(ope, *val)
            self.ui.bind_input_button(ope)

        self.ui.add_bind_eq_button(btn_row=6, btn_column=2, btn_span=2)
        self.ui.add_bind_clear_button(btn_row=6, btn_column=0, btn_span=2)
