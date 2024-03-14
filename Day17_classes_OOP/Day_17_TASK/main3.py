from data import question_data
from question_model import Question
from quizz_brain import QuizBrain, Kuiz_brain

question_bank = []

for entry in question_data:
    question = entry["question"]
    answer = entry["correct_answer"]
    difficulty = entry["difficulty"]
    category = entry["category"]
    new_question = Question(question, answer, difficulty=difficulty, category=category)
    question_bank.append(new_question)


number_of_correct_answers = 0

brain = Kuiz_brain(question_bank)
while brain.still_has_questions():
    brain.next_question()


print(f"\nYou completed the quiz\nYou've final score is {brain.correct_answers}/{brain.question_number}")