import random
import time

import pytest
from appium import webdriver

def setup_module(module, iii=int):
    """ setup any state specific to the execution of the given module."""
    print("\n===========test suite beginning=========================================")

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method."""
    driver.quit()
    print("\n===========test suite end================================================")

# set up appium
desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',desired_capabilities=desired_caps)

# other setup
delay = 1
wName = "Tola" + str(random.randint(1, 1000))
wSurname = "Testerka" + str(random.randint(1, 1000))
mName = "Tadek" + str(random.randint(1, 1000))
mSurname = "Tester" + str(random.randint(1, 1000))

def randomPesel(gender):
    # birth date
    p1 = random.randint(3, 9)
    p2 = random.randint(0, 9)
    p3 = random.randint(0, 2)
    p4 = random.randint(1, 9)
    p5 = random.randint(0, 1)
    p6 = random.randint(1, 7)
    pesel = str(p1) + str(p2) + str(p3) + str(p4) + str(p5) + str(p6)
    # + random number 000 - 999
    p7 = random.randint(0, 9)
    p8 = random.randint(0, 9)
    p9 = random.randint(0, 9)
    pesel = pesel + str(p7) + str(p8) + str(p9)
    # + gender
    if gender == "w":
        items = [0, 2, 4, 6, 8]
    else:
        items = [1, 3, 5, 7, 9]
    p10 = items[random.randrange(len(items))]
    pesel = pesel + str(p10)
    p11 = (9 * p1) + (7 * p2) + (3 * p3) + (1 * p4) + (9 * p5) + (7 * p6) + (3 * p7) + (1 * p8) + (9 * p9) + (7 * p10)
    p11 = p11 % 10
    pesel = pesel + str(p11)
    return pesel

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    print("\nThis is the begining of test case no _________________________________________________________")
    driver.find_element_by_name("Wyczyść wpis").click()
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    print("\nThis is the end of test case no _______________________________________________________________")


def getresults():
    displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
    displaytext = displaytext.strip("Wyświetlana wartość to ")
    displaytext = displaytext.rstrip(' ')
    displaytext = displaytext.lstrip(' ')
    return displaytext


class TestClass:

    def test_1addition(self):
        print("\n", wName, wSurname, "\t", mName, mSurname, "\n")
        for i in range(110):
            print(randomPesel("w"))
        driver.find_element_by_name("Jeden").click()
        driver.find_element_by_name("Plus").click()
        driver.find_element_by_name("Dwa").click()
        driver.find_element_by_name("Równa się").click()
        assert getresults() == "3", "test failed"
        time.sleep(delay)

    def test_2addition(self):
        driver.find_element_by_name("Jeden").click()
        driver.find_element_by_name("Plus").click()
        driver.find_element_by_name("Trzy").click()
        driver.find_element_by_name("Równa się").click()
        assert getresults() == "4", "test failed"
        time.sleep(delay)

    def test_3addition(self):
        # fail test
        driver.find_element_by_name("Jeden").click()
        driver.find_element_by_name("Plus").click()
        driver.find_element_by_name("Jeden").click()
        driver.find_element_by_name("Równa się").click()
        assert getresults() == "4", "test failed"
        time.sleep(delay)





