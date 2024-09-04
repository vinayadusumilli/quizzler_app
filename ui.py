from tkinter import *
from typing import Final

FONT: Final[tuple] = ("Arial", 10, "bold")


class Ui:
    def __init__(self, quiz_category, quiz_question) -> None:
        self.quiz_category = quiz_category
        self.quiz_question = quiz_question
        self.make_screen()

    def make_screen(self):
        # Window setup
        window = Tk()
        window.title(self.quiz_category)
        window.config(padx=50, pady=100)
        # Canvas setup
        canvas = Canvas(width=600, height=600, bg="green")
        canvas.create_text(300,200, text=self.quiz_question, fill="white", font=FONT)
        canvas.grid(row=0, column=0)

        window.mainloop()
