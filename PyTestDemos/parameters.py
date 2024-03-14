import pytest
import sys

@pytest.mark.parametrize("username, password",
                         [
                             ("Selenium","Webdriver"),
                             ("Python","Pytest"),
                             ("Mama", "Papa"),
                             ("Api", "Web")
                         ])
def test_login(username, password):
    print(username + password)