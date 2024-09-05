import html


class QuizBrain:
    def __init__(self, data):
        self.data = data
        self.current_question_number = 0
        self.score = 0
        self.current_question = ""
        self.current_answer = None
        self.current_question_category = ""
        self.next_question()

    def next_question(self):
        if self.current_question_number < len(self.data):
            self.current_question = html.unescape(self.data[self.current_question_number]["question"])
            self.current_answer = self.data[self.current_question_number]["correct_answer"]
            self.current_question_category = self.data[self.current_question_number]["category"]
            self.current_question_number += 1

    def update_score(self):
        pass
