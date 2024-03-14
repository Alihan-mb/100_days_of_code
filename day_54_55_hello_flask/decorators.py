color_list = ["red", "yellow", "green", "black", "blue", "orange", "purple", "pink", "brown", "grey"]


def make_h1(f):
    def wrapper():
        return f'<h1 style="color:{color_list}">' + f() + '</h1>'

    return wrapper




def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return '<u>' + function() + '</u>'

    return wrapper