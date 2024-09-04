from tkinter import *


class Ui:
    def __init__(self, quiz_category) -> None:
        self.quiz_category = quiz_category
        self.make_screen()

    def make_screen(self):
        window = Tk()
        window.title(self.quiz_category)

        window.mainloop()
