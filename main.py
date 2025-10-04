from mc_quiz import MultipleChoiceQuiz
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from mc_ui import MCQuizInterface
from ui import QuizInterface
from name import Name
import random
import subprocess
import os
from stat import S_IREAD, S_IWRITE
from summary import Summary


# ---------------------------------------------------------#
def get_summary():
    total = 2 * mc_quiz_ui.mc_score + quiz_ui.tf_score
    scores = ""

    scores = scores + f"\n{name_ui.name}\t{name_ui.section}"
    scores = scores + "\n---------------------------------------------------------"
    scores = scores + f"\nTest I: {quiz_ui.tf_score}"
    scores = scores + f"\nTest II: {mc_quiz_ui.mc_score} * 2 = {mc_quiz_ui.mc_score * 2}"
    scores = scores + f"\n\nFINAL SCORE: {total}/100"
    scores = scores + "\n---------------------------------------------------------"
    scores = scores + "\nRAISE YOUR HAND \nfor your score to be recorded."

    return scores


def write_final_scores():
    total = 2 * mc_quiz_ui.mc_score + quiz_ui.tf_score
    os.chmod("result.txt", S_IWRITE)
    with open("result.txt", "a") as file:
        file.write(f"\nFinal Score: {total}/100")
    os.chmod("result.txt", S_IREAD)


def show_multiple_choice():
    print("\n\nTest II. Type the letter of the correct answer.\n\nTwo(2) points each.\n[TYPE THE LETTER ONLY]\n")
    quiz_abcd = MultipleChoiceQuiz()
    total = 2 * quiz_abcd.abcd_score + quiz_ui.tf_score
    os.chmod("result.txt", S_IWRITE)
    with open("result.txt", "a") as file:
        file.write(f"\nFinal Score: {total}/100")
    os.chmod("result.txt", S_IREAD)
    print("---------------------------------------------------------")
    print("End of Test II")
    print("---------------------------------------------------------")
    print("\nYOUR SCORE:")
    print(f"Test I: {quiz_ui.tf_score}")
    print(f"Test II: {quiz_abcd.abcd_score * 2}")
    print(f"FINAL SCORE: {total}/100")
    print("---------------------------------------------------------")
    print("RAISE YOUR HAND SO THE PROCTOR CAN RECORD YOUR SCORE")
    message = input("While waiting you may type a message below...\n")
    os.chmod("result.txt", 666)
    with open("result.txt", "a") as file:
        file.write(f"\n{message}")

    subprocess.check_call(["attrib", "+H", "result.txt"])
    os.chmod("result.txt", S_IREAD)
    input("Press any key to exit...")


# ---------------------------------------------------------#

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer, [])
    question_bank.append(new_question)
    # if len(question_bank) == 2:
    #     break

name_ui = Name()
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
mc_quiz_ui = MCQuizInterface()
write_final_scores()
summary = Summary(get_summary())

# When done editing, compile by:
# open Terminal > then type the command
# pyinstaller main.py --onefile
