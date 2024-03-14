# number = [1, 2, 3]
# new_list = [n + 1 for n in number]
# print(new_list)

import pandas
#how to use loops over Pandas DataFrame

student_score = {
    "student": ["Angela", "Mark", "Ali"],
    "score": [78, 77, 90]
}

# for a, b in student_score.items():
#     print(a, b)

student_score_panda = pandas.DataFrame(student_score)

score_list = {row.student:row.score for index, row in student_score_panda.iterrows()}
print(score_list)