
def test_1():
    x = 10
    y = 10
    assert x == y, "It does not match"


def test_2():
    name = "selenium"
    title = "selenium is for web automation"
    assert name in title, "Name is not in title"

def test_3():
    name = "Jenkins"
    title = "jenkins is ci server"
    assert name in title, "Title does not match"
