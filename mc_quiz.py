import random

from data import question_MC
from question_model import Question
from quiz_brain import QuizBrain
from stat import S_IREAD


class MultipleChoiceQuiz:

    def __init__(self):
        self.abcd_score = 0
        self.mc_questions = []
        for question in question_MC:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            question_choices = question["incorrect_answers"]
            new_question = Question(question_text, question_answer, question_choices)
            self.mc_questions.append(new_question)
            # if len(self.mc_questions) == 2:
            #     break

        random.shuffle(self.mc_questions)

    def get_questions(self):
        return self.mc_questions
