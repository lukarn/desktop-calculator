import datetime
import json
import time

import pytest

from pywinauto.application import Application
from pywinauto.keyboard import send_keys

from commons.methods import *
from commons.param import *
from pages.Calc import *

import pyscreenshot


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
    x = datetime.datetime.now()
    x = x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + "_" + x.strftime("%X")
    print(x)


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

    def test_01print_con_ids(self):
        calc = Calc("Kalkulator")
        calc.get_ids(5)

    def test_02add(self):
        calc = Calc("Kalkulator")
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("num3Button")
        calc.set_button("Równa się")
        assert calc.get_result() == "4", "test failed"
        time.sleep(delay)

    def test_03add(self):
        calc = Calc("Kalkulator")
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("Pięć")
        calc.set_button("Równa się")
        assert calc.get_result() == "6", "test failed"
        time.sleep(delay)

    def test_04add(self):
        calc = Calc("Kalkulator")
        calc.click_1()
        calc.click_plus()
        calc.click_2()
        calc.click_equal()
        assert calc.get_result() == "3", "test failed"
        time.sleep(delay)

    def test_05add(self):
        calc = Calc("Kalkulator")
        send_keys("1234")
        calc.click_plus()
        send_keys("4321")
        calc.click_equal()
        assert calc.get_result() == "5555", "test failed"
        time.sleep(delay)

    def test_06add(self):
        calc = Calc("Kalkulator")
        send_keys(data["num1"][0])
        calc.click_plus()
        send_keys(data["num2"][0])
        calc.click_equal()
        assert calc.get_result() == data["add"][0], "test failed"
        time.sleep(delay)

    def test_07add(self):
        calc = Calc("Kalkulator")
        send_keys(data["num1"][1])
        send_keys("{VK_ADD}")
        send_keys(data["num2"][1])
        send_keys("{ENTER}")
        assert calc.get_result() == data["add"][1], "test failed"
        time.sleep(delay)

    def test_08add(self):
        calc = Calc("Kalkulator")
        send_keys(data["num1"][2])
        calc.click_plus()
        send_keys(data["num2"][2])
        calc.click_equal()
        assert calc.get_result() == data["add"][2], "test failed"
        time.sleep(delay)

    def test_09add(self):
        calc = Calc("Kalkulator")
        send_keys(data["num1"][3])
        calc.click_plus()
        send_keys(data["num2"][3])
        calc.click_equal()
        assert calc.get_result() == data["add"][3], "test failed"
        time.sleep(delay)

    def test_10add(self):
        calc = Calc("Kalkulator")
        send_keys(data["num1"][4])
        calc.click_plus()
        send_keys(data["num2"][4])
        calc.click_equal()
        assert calc.get_result() == data["add"][4], "test failed"
        time.sleep(delay)

    def test_11add(self):
        # failure test
        calc = Calc("Kalkulator")

        # grab fullscreen
        im = pyscreenshot.grab()
        # save image file
        im.save("../screenshots/screenshot.png")

        assert calc.get_result() == data["add"][4], "test failed"
        time.sleep(delay)
