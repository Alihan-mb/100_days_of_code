from data import question_data
from question_model import Question
from quizz_brain import QuizBrain

question_bank = []


for entry in question_data:
    question = entry["text"]
    answer = entry["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)


number_of_correct_answers = 0

brain = QuizBrain(question_bank)

is_on = True
while is_on:
    if brain.question_number != 12:
        user_answer = brain.next_question()
        right_answer = brain.right_answer()
        if user_answer == right_answer:
            print("You got it right!")
            print(f"The correct answer was: {right_answer}")
            number_of_correct_answers += 1
            print(f"Your current score is {number_of_correct_answers}/{brain.question_number}")
        else:
            print("That's wrong.")
            print(f"The correct answer was {right_answer}")
            print(f"Your current score is {number_of_correct_answers}/{brain.question_number}")
    else:
        print(f"Those are all the questions, your final score is: {number_of_correct_answers}/{brain.question_number}")
        is_on = False