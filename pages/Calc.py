from pywinauto import Desktop

class Calc:

    # parameterized constructor
    def __init__(self, windowName):
        self.windowName = Desktop(backend="uia").window(best_match=windowName)

    def setButton(self, buttonTitle):
        self.windowName.window(title=buttonTitle, control_type="Button").click()

    # zrobić duży blok try który będzie próbować kliknąć w kilka różnych opcji - wystarczy, że jeden z nich będzie dobry to będzie ok;
    # np try {self.windowName.window(title=buttonTitle, control_type="Button").click() ....}, try{self.windowName.window(class=buttonTitle, control_type="Button").click()}
    # jeżeli już jakiś kliknie to kolejnych nie sprawdza