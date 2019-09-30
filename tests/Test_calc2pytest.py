import time

import pytest
from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto import findbestmatch

from commons.methods import *
from commons.param import *


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
    awindow["Zamknij aplikację Kalkulator"].click()
    print("\n===========test suite end================================================")


# application
app = Application(backend="uia").start("C:\Windows\System32\calc.exe")
awindow = Desktop(backend="uia").Kalculator

# other setup -> random man&woman
wName = "Tola" + str(random.randint(1, 1000))
wSurname = "Testerka" + str(random.randint(1, 1000))
mName = "Tadek" + str(random.randint(1, 1000))
mSurname = "Tester" + str(random.randint(1, 1000))


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code before each test case
    print("\nThis is the begining of test case no _________________________________________________________")
    awindow["Wyczyść wpis"].click()
    yield
    # Code after each test case
    print("\nThis is the end of test case no _______________________________________________________________")


def getresults():
    calcResult = awindow['.*Wyświetlana wartość to.*'].texts()
    calcResult = ''.join(calcResult)
    calcResult = calcResult.strip("Wyświetlana wartość to ")
    return calcResult


class Test_calc2pytest:

    def test_1printConIds(self):
        awindow.print_control_identifiers(depth=5)

    def test_2add(self):
        awindow.Jeden.click()
        awindow.Plus.click()
        awindow.Trzy.click()
        awindow["Równa się"].click()
        getresults()
        assert getresults() == "4", "test failed"
        time.sleep(delay)

    def test_3addPyWin(self):
        awindow.window(auto_id='num1Button', class_name='Button').click()
        awindow.Plus.click()
        awindow.window(title='Trzy', control_type="Button").click()  # title = name
        awindow["Równa się"].click()
        getresults()
        assert getresults() == "4", "test failed"
        time.sleep(delay)

    def test_3addPyWin(self):
        awindow.window(auto_id='num1Button', class_name='Button').click()
        awindow.Plus.click()
        awindow.window(title='Trzy', control_type="Button").click()  # title = name
        awindow["Równa się"].click()
        getresults()
        assert getresults() == "4", "test failed"
        time.sleep(delay)

    def test_4addPyWinObjectTexts(self):
        awindow.window(auto_id='num1Button', class_name='Button').click()
        awindow.Plus.click()
        awindow.window(title='Trzy', control_type="Button").click()  # title = name
        awindow["Równa się"].click()

        # find_best_match(search_text, item_texts, items, limit_ratio=0.5)
        # found_item = awindow.findbestmatch.find_best_match('Button6', 'Button6')
        # texts = awindow.texts()[1:]  # skip window text itself, use only item texts
        # texts = awindow.texts()  # skip window text itself, use only item texts
        # items = awindow.items()

        # found_item = awindow.findbestmatch.find_best_match('Button6', texts, items)

        # awindow.window(best_match='Button6').click()



        # The list of texts to search through:
        # texts = awindow.window(title="Klawiatura numeryczna").print_control_identifiers(depth=5)
        # texts = awindow.window(title="Klawiatura numeryczna").texts()[1:]  # skip window text itself
        # print(">>>>>>>>>>>>teksts>>>>>>>>>>>>>>>", texts, "<<<<<<<<<<<<<<<<<<<<<<<")
        # # The list of items corresponding (1 to 1) to the list of texts to search through.
        # items = awindow.window(title="Klawiatura numeryczna").items()  # >>[]
        # print(">>>>>>>>>>>>items>>>>>>>>>>>>>>>", items, "<<<<<<<<<<<<<<<<<<<<<<<")
        # found_item = findbestmatch.find_best_match('Button5', texts, items, limit_ratio=0.1).Select()
        # found_item.click()



        getresults()
        assert getresults() == "4", "test failed"
        time.sleep(delay)
