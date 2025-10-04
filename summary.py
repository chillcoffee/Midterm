from tkinter import *

THEME_COLOR = "#92664A"


class Summary:

    def __init__(self, q_text):
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        quote = "Good programmers doesn't worry about the code, \nbut they problem more about the data structure and their relationships.\n~Linus Torvalds"

        self.window.title("CC 105 MIDTERM EXAM")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text=quote, fg="WHITE", bg=THEME_COLOR, font=("Monotype Corsiva", 14, "italic"))
        self.label_score.grid(row=0, column=0, pady=20)

        quote = "And someday you will be that good programmer.\nCongratulations and good luck!\n~Ma'am Ruffa"
        self.label_score = Label(text=quote, fg="WHITE", bg=THEME_COLOR, font=("Monotype Corsiva", 14, "italic"))
        self.label_score.grid(row=2, column=0, pady=20)

        self.canvas = Canvas(width=550, height=250, bg="WHITE")
        self.canvas.grid(row=1, column=0, pady=20)

        self.question_text = self.canvas.create_text(
            270, 115,
            width=450,
            text=q_text,
            fill=THEME_COLOR,
            font=("Times", 16, "normal"),
            anchor="center"
        )

        self.window.resizable(False, False)
        width = 600
        height = 550

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.mainloop()
