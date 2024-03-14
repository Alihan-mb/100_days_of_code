import pytest
from selenium import webdriver

driver = None
@pytest.fixture()
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("Close the browser")

def test_1(setup):
    driver.get("http://www.google.com")
    print("Test 1 executed")

def test_2(setup):
    driver.get("https://docs.pytest.org/en/stable/contents.html")
    print("Test 2 executed")

def test_3(setup):
    driver.get("https://wikipedia.com")
    print("Test 3 executed")



















""""""
        #Preconditions
            #Setup, connection, API

        #Test

        #Test

        #Assertion

        #Postcon
            #Clean, close, close


""""""