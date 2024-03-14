def going():
    print("73")


def moving():
    print("________________________________")


def one_turn_left():
    print("_______________________________")


moves = 0
for i in range(1, 100):
    moves += 1
    if moves <= 73:
        moving()
        one_turn_left()
        moving()
        going()
        moving()
        going()
        moving()
        one_turn_left()
    else:
        print("that's all")
        exit()