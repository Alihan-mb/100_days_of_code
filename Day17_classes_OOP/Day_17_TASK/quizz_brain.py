class QuizBrain:
    '''Первый класс, где я сам закончил задание'''
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)? ").lower()
        return user_answer

    def right_answer(self):
        answer = self.question_list[self.question_number - 1].answer
        return answer.lower()



class Kuiz_brain:
    '''Новый класс который был создан для тестирования, правильная реализация тут'''
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_answers = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.difficulty}, {question.category}: {question.text} (True/False)? ").lower()
        self.right_answer(user_answer, question.answer)

    def right_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.correct_answers += 1
            print(f"Your current score is {self.correct_answers}/{self.question_number}")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.correct_answers}/{self.question_number}")
        print("\n")