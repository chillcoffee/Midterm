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
            # if len(self.mc_questions) == 5:
            #     break

        random.shuffle(self.mc_questions)

    def get_questions(self):
        return self.mc_questions

    def write_score(self):
        import os
        os.chmod("result.txt", 666)
        with open("result.txt", mode="a") as file:
            file.write(f"\n\nTest II. Multiple Choice\nScore: {self.quiz.score * 2}\n")
        os.chmod("result.txt", S_IREAD)
        self.abcd_score = self.quiz.score
