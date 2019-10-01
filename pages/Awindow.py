from pywinauto import Desktop


class Awindow:
    awindow = None

    # parameterized constructor
    def __init__(self, windowName, buttonTitle):
        self.awindow = Desktop(backend="uia").window(best_match=windowName).window(title=buttonTitle, control_type="Button")