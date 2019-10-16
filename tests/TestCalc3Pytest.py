import json
import time
from commons.methods import *
from commons.param import *
from pages.Calc import *


# jsondata import
with open("../jsondata/add_test.json", "r") as read_file:
    data = json.load(read_file)


# page object for all tests
calc = Calc("Kalkulator")


class TestCalc3Pytest:

    def test_01print_con_ids(self):
        calc.get_ids(5)
        time.sleep(delay)

    def test_02add(self):
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("num3Button")
        calc.set_button("Równa się")
        assert calc.get_result() == "4", "test failed"

    def test_03add(self):
        calc.set_button("Jeden")
        calc.set_button("Plus")
        calc.set_button("Pięć")
        calc.set_button("Równa się")
        assert calc.get_result() == "6", "test failed"
        time.sleep(delay)

    def test_04add(self):
        calc.click_1()
        calc.click_plus()
        calc.click_2()
        calc.click_equal()
        assert calc.get_result() == "3", "test failed"

    def test_05add(self):
        send_keys("1234")
        calc.click_plus()
        send_keys("4321")
        calc.click_equal()
        assert calc.get_result() == "5555", "test failed"

    def test_06add(self):
        send_keys(data["num1"][0])
        calc.click_plus()
        send_keys(data["num2"][0])
        calc.click_equal()
        assert calc.get_result() == data["add"][0], "test failed"

    def test_07add(self):
        send_keys(data["num1"][1])
        send_keys("{VK_ADD}")
        send_keys(data["num2"][1])
        send_keys("{ENTER}")
        assert calc.get_result() == data["add"][1], "test failed"

    def test_08add(self):
        send_keys(data["num1"][2])
        calc.click_plus()
        send_keys(data["num2"][2])
        calc.click_equal()
        assert calc.get_result() == data["add"][2], "test failed"

    def test_09add(self):
        assert calc.add_2(data["num1"][3], data["num2"][3]) == data["add"][3], "test failed"

    def test_10add(self):
        assert calc.add_2(data["num1"][4], data["num2"][4]) == data["add"][4], "test failed"

    def test_11add(self):
        # failure test - screenshot after failure
        send_keys(random_pesel("m"))
        calc.click_plus()
        send_keys(random_pesel("w"))
        calc.click_equal()
        assert calc.get_result() == data["add"][4], "test failed"
