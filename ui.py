import os
from tkinter import *

from quiz_brain import QuizBrain
from stat import S_IREAD, S_IWRITE

THEME_COLOR = "#92664A"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.tf_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')

        self.window.title("Test I. True or False")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: ", fg="WHITE", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.label_score.grid(row=0, column=3, pady=20)

        self.canvas = Canvas(width=350, height=250, bg="WHITE")
        self.canvas.grid(row=1, column=0, columnspan=4, pady=20)
        self.question_text = self.canvas.create_text(
            180, 125,
            width=320,
            text="Some Question Text",
            fill="black",
            font=("Calibri", 18, "italic")
        )

        false_img = PhotoImage(file="false.png")
        true_img = PhotoImage(file="true.png")

        next_img = PhotoImage(file="next.png")

        self.button_false = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.click_true)

        self.button_false.grid(row=2, column=2, pady=20, padx=10)
        self.button_true.grid(row=2, column=1, pady=20, padx=10)

        self.button_next = Button(image=next_img, highlightthickness=0, command=self.click_next)

        self.button_next.grid(row=2, column=3, pady=20, padx=10)

        self.get_next_question()
        self.window.resizable(False, False)
        width = 410
        height = 550

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.mainloop()

    def get_next_question(self):
        self.label_score.config(text=f"Score: {self.quiz.score} / {len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        elif len(self.quiz.skipped_list) != 0:
            self.canvas.config(bg="white")
            q_text = self.quiz.next_skipped_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.tf_score = self.quiz.score
            os.chmod("result.txt", S_IWRITE)
            with open("result.txt", mode="a") as file:
                file.write(f"\n\nTest I. True or False\nScore: {self.quiz.score}\n")
            os.chmod("result.txt", S_IREAD)
            self.canvas.itemconfig(self.question_text,
                                   text=f"Your score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.canvas.config(bg="white")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.button_next.config(state="disabled")

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_next(self):
        # put the current question in skipped_list
        question = self.canvas.itemcget(self.question_text, 'text')
        item = question[0]

        self.quiz.skipped_numbers.append(item)
        self.quiz.skipped_list.append(self.quiz.current_question)

        if len(self.quiz.skipped_list) == 1 and self.quiz.still_has_questions() == False:
            self.button_next.config(state="disabled")
        # get next question
        self.get_next_question()

    def click_prev(self):
        # get the first question in skipped_list
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
