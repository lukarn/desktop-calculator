import json
import time

import pytest

from pywinauto.application import Application

from commons.methods import *
from commons.param import *
from pages.Calc import *


def setup_module():
    """ setup any state specific to the execution of the given module."""
    print("\n===========test suite beginning=========================================")
    print("Random string data: ")
    print(wName, wSurname, "\t", mName, mSurname)
    for i in range(2):
        print(randomPesel("w"))
    print("num1: " + data["num"])
    print(data["num1"])
    print(data["num1"][0])


def teardown_module():
    """ teardown any state that was previously setup with a setup_module
    method."""
    calc = Calc("Kalkulator")
    calc.set_button("Zamknij aplikację Kalkulator")
    print("\n===========test suite end================================================")


# application
app = Application(backend="uia").start("C:\\Windows\\System32\\calc.exe")

# other setup -> random man&woman
wName = "Tola" + str(random.randint(1, 1000))
wSurname = "Testerka" + str(random.randint(1, 1000))
mName = "Tadek" + str(random.randint(1, 1000))
mSurname = "Tester" + str(random.randint(1, 1000))

# global no_test
no_test = 0

# jsondata import
with open("../jsondata/add_test.json", "r") as read_file:
    data = json.load(read_file)


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code before each test case
    global no_test
    no_test = no_test + 1
    print(
        "\nThis is the begining of test case no {0} _________________________________________________".format(no_test))
    calc = Calc("Kalkulator")
    calc.set_button("Wyczyść wpis")
    yield
    # Code after each test case
    print("\nThis is the end of test case no {0} _____________________________________________________".format(no_test))


class TestCalc3Pytest:

    def test_1print_con_ids(self):
        calc = Calc("Kalkulator")
        calc.get_ids(5)

    def test_2add(self):
        calc = Calc("Kalkulator")
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("num3Button")
        calc.set_button("Równa się")
        assert calc.get_result() == "4", "test failed"
        time.sleep(delay)

    def test_3add(self):
        calc = Calc("Kalkulator")
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("Pięć")
        calc.set_button("Równa się")
        assert calc.get_result() == "6", "test failed"
        time.sleep(delay)

    def test_4add(self):
        calc = Calc("Kalkulator")
        calc.click_1()
        calc.click_plus()
        calc.click_2()
        calc.click_equal()
        assert calc.get_result() == "3", "test failed"
        time.sleep(delay)

    def test_5add(self):
        # a = True
        # b = False
        calc = Calc("Kalkulator")
        calc.click_1()
        calc.click_plus()
        calc.click_2()
        calc.click_equal()
        assert calc.get_result() == "3", "test failed"
        time.sleep(delay)
