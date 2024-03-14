enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

'''Global constants'''
PI = 3.14159
URL = "http://me.com"

def cacl():
    list.append(URL)

