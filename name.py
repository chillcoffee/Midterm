import os
from tkinter import *
from stat import S_IREAD, S_IWRITE

# THEME_COLOR = "#fb8da0"       #PINK for EMC
THEME_COLOR = "#765341"  # BROWN for BSIS


class Name:

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def __init__(self):
        self.name = ""
        self.section = ""
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')

        self.window.title("Midterm Exam CC 104")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, width=600, height=400)
        self.window.resizable(False, False)
        self.label_name = Label(text="Name: ", fg="WHITE", bg=THEME_COLOR,
                                font=("Arial", 14, "bold"))
        self.label_name.grid(row=0, column=0, pady=20)

        self.entry_name = Entry(width=30, font=("Arial", 14, "bold"))
        self.entry_name.grid(row=0, column=1, pady=20)

        self.label_yr_section = Label(text="Yr - Major: ", fg="WHITE", bg=THEME_COLOR,
                                      font=("Arial", 14, "bold"))
        self.label_yr_section.grid(row=1, column=0, pady=20)

        self.entry_yr_section = Entry(width=30, font=("Arial", 14, "bold"))
        self.entry_yr_section.grid(row=1, column=1, pady=20)

        self.button_submit = Button(text="START", highlightthickness=0, command=self.submit, font=("Arial", 14, "bold"),
                                    fg=THEME_COLOR)
        self.button_submit.grid(row=4, column=0, pady=20, columnspan=2)
        width = self.window.winfo_width()
        height = self.window.winfo_height()

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{500}x{250}+{x}+{y}")
        self.window.mainloop()

    def submit(self):
        os.chmod("result.txt", S_IWRITE)
        self.name = self.entry_name.get()
        self.section = self.entry_yr_section.get()
        with open("result.txt", "a") as f:
            f.write(f"\n\n---------------------------------------------------------\n")
            f.write(f"Name: {self.name}\n")
            f.write(f"Yr & Section: {self.entry_yr_section.get()}")
        os.chmod("result.txt", S_IREAD)
        self.window.destroy()
