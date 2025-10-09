import os
import pyautogui
from tkinter import *

from quiz_brain import QuizBrain
from mc_quiz import MultipleChoiceQuiz
from stat import S_IREAD, S_IWRITE

# THEME_COLOR = "#fb8da0"       #PINK for EMC
THEME_COLOR = "#765341"  # BROWN for BSIS


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
            25, 20,
            width=500,
            text="Some Question Text",
            fill="black",
            font=("Calibri", 12, "italic"),
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
        self.check_mouse_position()
        self.window.mainloop()

    def check_mouse_position(self):
        # Get mouse coordinates
        mx, my = pyautogui.position()

        # Get total window and client area bounds
        self.window.update_idletasks()
        win_x = self.window.winfo_rootx()
        win_y = self.window.winfo_rooty()
        client_x = self.window.winfo_x()
        client_y = self.window.winfo_y()
        width = self.window.winfo_width()
        height = self.window.winfo_height()

        # Compute title bar height and border width
        titlebar_height = win_y - client_y
        border_width = win_x - client_x

        # Define client (usable) area boundaries
        x1 = win_x + border_width
        y1 = win_y + titlebar_height
        x2 = x1 + width - (2 * border_width)
        y2 = y1 + height - border_width

        # Only move the mouse back if it left the client area
        if not (x1 <= mx <= x2 and y1 <= my <= y2):
            # But ignore top title bar zone (minimize, close, drag)
            if not (win_x <= mx <= win_x + width and win_y - 10 <= my <= y1):
                # Move to center of window
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                pyautogui.moveTo(cx, cy, duration=0.1)

        # Recheck after 100ms
        self.window.after(5000, self.check_mouse_position)

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
            self.canvas.coords(self.question_text, 80, 80)
            self.canvas.itemconfig(self.question_text, anchor="nw",
                                   font=("Times", 18, "normal"), fill=THEME_COLOR,
                                   text=f"Test II (2 points each)\nScore: {self.quiz.score * 2} / {len(self.quiz.question_list) * 2}\n\nClose this window to see your FINAL SCORE.")
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
        dot_index = question.index(".")
        item = question[:dot_index]

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
