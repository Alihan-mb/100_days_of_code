score = 0

def mama(score):
    score +=1
    return score


i = 0
while 5 > i:
    score = mama(score)
    print(score)
    i +=1