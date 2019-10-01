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
    # awindow["Zamknij aplikację Kalkulator"].click()
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
    # awindow["Wyczyść wpis"].click()
    yield
    # Code after each test case
    print("\nThis is the end of test case no _______________________________________________________________")


# def getresults():
#     calcResult = awindow['.*Wyświetlana wartość to.*'].texts()
#     calcResult = ''.join(calcResult)
#     calcResult = calcResult.strip("Wyświetlana wartość to ")
#     return calcResult


class Test_calc2pytest:

    # def test_1printConIds(self):
    #     awindow.print_control_identifiers(depth=5)

    def test_2add(self):
        calc = Calc("Kalkulator")
        calc.setButton("Jeden")
        # awindow.Jeden.click()
        # awindow.Plus.click()
        # awindow.Trzy.click()
        # awindow["Równa się"].click()
        # getresults()
        # assert getresults() == "4", "test failed"
        time.sleep(delay)

