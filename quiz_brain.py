import html
import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.skipped_numbers = []
        self.skipped_list = []
        self.current_question = None
        self.correct_letter = 'E'

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"{self.question_number}. {q_text}"

    def next_skipped_question(self):
        self.current_question = self.skipped_list.pop(0)
        skipped_number = self.skipped_numbers.pop(0)
        q_text = html.unescape(self.current_question.text)
        return f"{skipped_number}. {q_text}"

    def printChoices(self, choices):
        random.shuffle(choices)
        shuffled_choices = f"\n\nA. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}"
        for i in range(0, 4):
            if choices[i] == self.current_question.answer:
                self.correct_letter = chr(65 + i)
        return shuffled_choices

    def show_mcquestion(self, ):
        """for multiple choice"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)

        q_text = f"{self.question_number}. {q_text}"

        choices_list = self.current_question.choices
        shuffled_choices = self.printChoices(choices_list)
        q_text = q_text + shuffled_choices
        return q_text

    def next_skipped_mcquestion(self):
        self.current_question = self.skipped_list.pop(0)
        skipped_number = self.skipped_numbers.pop(0)
        # print skipped items
        # print(f"skipped items: {self.skipped_numbers}")
        q_text = html.unescape(self.current_question.text)
        q_text = f"{skipped_number}. {q_text}"
        choices_list = self.current_question.choices
        shuffled_choices = self.printChoices(choices_list)
        q_text = q_text + shuffled_choices
        return q_text

    def check_answerInput(self, user_answer, correct_letter):
        correct_answer = correct_letter
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_mcanswer(self, user_answer):
        if user_answer.lower() == self.correct_letter.lower():
            self.score += 1
            return True
        else:
            return False

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
