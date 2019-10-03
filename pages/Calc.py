import logging

from pywinauto import Desktop


class Calc:

    # LOCATORS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def jeden(self):
        return self.window_name.Jeden

    def dwa(self):
        return self.window_name.Dwa

    def trzy(self):
        return self.window_name.Trzy

    def cztery(self):
        return self.window_name.Cztery

    def piec(self):
        return self.window_name.Pięć

    def szesc(self):
        return self.window_name.Sześć

    def siedem(self):
        return self.window_name.Siedem

    def osiem(self):
        return self.window_name.Osiem

    def dziewiec(self):
        return self.window_name.Dziewięć

    def zero(self):
        return self.window_name.Zero

    def plus(self):
        return self.window_name.Plus

    def rownasie(self):
        return self.window_name.window(title="Równa się", control_type="Button")

    # END OF LOCATORS !!!!!!!!!!!!!!!!!!!!!!!!!

    # parameterized constructor
    def __init__(self, window_name):
        self.window_name = Desktop(backend="uia").window(best_match=window_name)

    def set_button_by_title(self, button_title):
        self.window_name.window(title=button_title, control_type="Button").click()

    def set_button(self, button_name):
        try:
            self.window_name.window(title=button_name, control_type="Button").click()
        except Exception as e1:
            logging.exception(e1)
            try:
                self.window_name.window(auto_id=button_name, class_name="Button").click()
            except Exception as e:
                print("!!!!!!!No such button!!!!!!!!!")
                logging.exception(e)

    def get_result(self):
        result = self.window_name.window(auto_id="CalculatorResults", control_type="Text").texts()
        result = ''.join(result)
        result = result.strip("Wyświetlana wartość to ")
        return result

    def get_ids(self, level):
        self.window_name.print_control_identifiers(depth=level)

    # click number (0-9)
    def click_1(self):
        self.jeden().click()

    def click_2(self):
        self.dwa().click()

    def click_3(self):
        self.trzy().click()

    def click_4(self):
        self.cztery().click()

    def click_5(self):
        self.piec().click()

    def click_6(self):
        self.szesc().click()

    def click_7(self):
        self.siedem().click()

    def click_8(self):
        self.osiem().click()

    def click_9(self):
        self.dziewiec().click()

    def click_0(self):
        self.zero().click()

    def click_plus(self):
        self.plus().click()

    def click_equal(self):
        self.rownasie().click()
