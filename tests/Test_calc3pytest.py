import time

import pytest
from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto import findbestmatch

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


def teardown_module():
    """ teardown any state that was previously setup with a setup_module
    method."""
    calc = Calc("Kalkulator")
    calc.setButton("Zamknij aplikację Kalkulator")
    print("\n===========test suite end================================================")


# application
app = Application(backend="uia").start("C:\Windows\System32\calc.exe")

# other setup -> random man&woman
wName = "Tola" + str(random.randint(1, 1000))
wSurname = "Testerka" + str(random.randint(1, 1000))
mName = "Tadek" + str(random.randint(1, 1000))
mSurname = "Tester" + str(random.randint(1, 1000))


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code before each test case
    print("\nThis is the begining of test case no _________________________________________________________")
    calc = Calc("Kalkulator")
    calc.setButton("Wyczyść wpis")
    yield
    # Code after each test case
    print("\nThis is the end of test case no _______________________________________________________________")


class Test_calc2pytest:

    def test_1printConIds(self):
        calc = Calc("Kalkulator")
        calc.getids(5)

    def test_1add(self):
        calc = Calc("Kalkulator")
        calc.setButton("Jeden")
        calc.setButton("Plus")
        calc.setButton("num3Button")
        calc.setButton("Równa się")
        assert calc.getResult() == "4", "test failed"
        time.sleep(delay)

    def test_2add(self):
        calc = Calc("Kalkulator")
        calc.setButton("Jeden")
        calc.setButton("Plus")
        calc.setButton("Pięć")
        calc.setButton("Równa się")
        assert calc.getResult() == "6", "test failed"
        time.sleep(delay)

