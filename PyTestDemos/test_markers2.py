import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.skipif(condition=sys.version_info < (3, 12), reason="Python version not supported")
def test_addproduct():
    print("Add products")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")

@pytest.mark.parametrize
def test_close():
    assert True
    print("Close the app")