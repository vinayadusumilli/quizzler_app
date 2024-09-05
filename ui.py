from tkinter import *
from typing import Final
from brain import QuizBrain

FONT: Final[tuple] = ("Arial", 20, "bold")
BACKGROUND_COLOR: Final[str] = '#55679C'


class Interface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title(f"Quiz Category ==> {quiz_brain.current_question_category}")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        # Label for ScoreCard
        self.score_label = Label(text=f"Score: {self.quiz_brain.score}", bg=BACKGROUND_COLOR, font=FONT)
        self.score_label.grid(row=0, column=1)
        # Canvas setup to display quiz questions
        self.canvas = Canvas(width=400, height=500, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(200, 200, text=quiz_brain.current_question,
                                                   fill="black", font=FONT, width=350)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        # Buttons to choose True/False
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(width=75, height=75, pady=100, padx=100,
                                  image=self.true_image, command=self.true_clicked)
        self.false_button = Button(width=75, height=75, pady=100, padx=100,
                                   image=self.false_image, command=self.false_clicked)
        self.true_button.grid(row=3, column=0)
        self.false_button.grid(row=3, column=1)

        self.window.mainloop()

    def true_clicked(self):
        self.quiz_brain.next_question()
        self.canvas.itemconfig(self.canvas_text, text=self.quiz_brain.current_question)

    def false_clicked(self):
        self.quiz_brain.next_question()
