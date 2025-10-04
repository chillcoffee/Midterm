import os
from tkinter import *

from quiz_brain import QuizBrain
from mc_quiz import MultipleChoiceQuiz
from stat import S_IREAD, S_IWRITE

THEME_COLOR = "#92664A"


class MCQuizInterface:

    def __init__(self):
        self.mcq = MultipleChoiceQuiz()
        self.question_bank = self.mcq.get_questions()
        self.quiz = QuizBrain(self.question_bank)
        self.mc_score = 0
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')

        self.window.title("Test II. Multiple Choice (2 pts each)")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: ", fg="WHITE", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.label_score.grid(row=0, column=4, pady=20)

        self.canvas = Canvas(width=550, height=250, bg="WHITE")
        self.canvas.grid(row=1, column=0, columnspan=5, pady=20)
        self.question_text = self.canvas.create_text(
            25, 50,
            width=500,
            text="Some Question Text",
            fill="black",
            font=("Calibri", 14, "italic"),
            anchor="nw"
        )
        a_img = PhotoImage(file="A.png")

        b_img = PhotoImage(file="B.png")
        c_img = PhotoImage(file="C.png")
        d_img = PhotoImage(file="D.png")
        next_img = PhotoImage(file="next.png")

        self.button_A = Button(image=a_img, highlightthickness=0, command=self.click_A)
        self.button_A.grid(row=2, column=0, pady=20, padx=10)

        self.button_C = Button(image=c_img, highlightthickness=0, command=self.click_C)
        self.button_B = Button(image=b_img, highlightthickness=0, command=self.click_B)

        self.button_C.grid(row=2, column=2, pady=20, padx=10)
        self.button_B.grid(row=2, column=1, pady=20, padx=10)

        self.button_D = Button(image=d_img, highlightthickness=0, command=self.click_D)
        self.button_D.grid(row=2, column=3, pady=20, padx=10)

        self.button_skip = Button(image=next_img, highlightthickness=0, command=self.click_next)
        self.button_skip.grid(row=2, column=4, pady=20, padx=10)

        self.get_next_question()
        self.window.resizable(False, False)
        width = 660
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
            q_text = self.quiz.show_mcquestion()
            self.canvas.itemconfig(self.question_text, text=q_text)
        elif len(self.quiz.skipped_list) != 0:
            self.canvas.config(bg="white")
            q_text = self.quiz.next_skipped_mcquestion()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.mc_score = self.quiz.score
            os.chmod("result.txt", S_IWRITE)
            with open("result.txt", mode="a") as file:
                file.write(f"\n\nTest II. Multiple Choice\nScore: {self.quiz.score * 2}\n")
            os.chmod("result.txt", S_IREAD)
            self.canvas.coords(self.question_text, 100, 100)
            self.canvas.itemconfig(self.question_text, anchor="nw",
                                   font=("Times", 18, "normal"), fill=THEME_COLOR,
                                   text=f"Test II (2 points each)\nScore: {self.quiz.score * 2} / {len(self.quiz.question_list) * 2}")
            self.canvas.config(bg="white")
            self.button_A.config(state="disabled")
            self.button_B.config(state="disabled")
            self.button_C.config(state="disabled")
            self.button_D.config(state="disabled")
            self.button_skip.config(state="disabled")

    def click_A(self):
        is_right = self.quiz.check_mcanswer("A")
        self.give_feedback(is_right)

    def click_B(self):
        is_right = self.quiz.check_mcanswer("B")
        self.give_feedback(is_right)

    def click_C(self):
        is_right = self.quiz.check_mcanswer("C")
        self.give_feedback(is_right)

    def click_D(self):
        self.give_feedback(self.quiz.check_mcanswer("D"))

    def click_next(self):
        # put the current question in skipped_list
        question = self.canvas.itemcget(self.question_text, 'text')
        item = question[0]  # get the item #

        self.quiz.skipped_numbers.append(item)
        self.quiz.skipped_list.append(self.quiz.current_question)

        # print skipped numbers
        # print(f"iniside next: {self.quiz.skipped_numbers}")

        if len(self.quiz.skipped_list) == 1 and self.quiz.still_has_questions() == False:
            self.button_skip.config(state="disabled")
        # get next question
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
