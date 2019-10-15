import json
import time
from pywinauto.keyboard import send_keys
from commons.methods import *
from commons.param import *
from pages.Calc import *


# other setup -> random man&woman
# data used in other tests - here just exercises
wName = "Tola" + str(random.randint(1, 1000))
wSurname = "Testerka" + str(random.randint(1, 1000))
wPesel = random_pesel("w")
mName = "Tadek" + str(random.randint(1, 1000))
mSurname = "Tester" + str(random.randint(1, 1000))
mPesel = random_pesel("m")


# jsondata import
with open("../jsondata/add_test.json", "r") as read_file:
    data = json.load(read_file)


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
        assert calc.get_result() == data["add"][4], "test failed"
        time.sleep(delay)
