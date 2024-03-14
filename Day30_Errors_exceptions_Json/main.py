
try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
else:
    print("FFF")
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

try:
    a_dict = {"key": "value"}
    print(a_dict["mama"])
except KeyError as error:
    print(f"there is no key like {error}")
