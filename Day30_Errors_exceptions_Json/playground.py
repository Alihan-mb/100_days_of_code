try:
    a_list = ["as", "bb", "tt"]
    print(a_list[6])
except IndexError:
    print("There is no item at that index")
try:
    a_dict = {"mother": "father"}
    print(a_dict["grandpa"])
except KeyError:
    print("Key does not exist in the dictionary")

try:
    print(a_list[10])
    print(a_dict["fsadfsdaf"])
except Exception as e:
    print(e)


