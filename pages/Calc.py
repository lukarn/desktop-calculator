from pywinauto import Desktop

class Calc:

    # parameterized constructor
    def __init__(self, windowName):
        self.windowName = Desktop(backend="uia").window(best_match=windowName)

    def setButtonByTitle(self, buttonTitle):
        self.windowName.window(title=buttonTitle, control_type="Button").click()

    def setButton(self, buttonName):
        try:
            self.windowName.window(title=buttonName, control_type="Button").click()
        except:
            try:
                self.windowName.window(auto_id=buttonName, class_name="Button").click()
            except:
                print("!!!!!!!No such button!!!!!!!!!")

    def getResult(self):
        calcResult = self.windowName.window(auto_id="CalculatorResults", control_type="Text").texts()
        calcResult = ''.join(calcResult)
        calcResult = calcResult.strip("Wyświetlana wartość to ")
        return calcResult

    def getids(self, level):
        self.windowName.print_control_identifiers(depth=level)


