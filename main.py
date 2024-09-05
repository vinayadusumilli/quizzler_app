from api_data import Data
from ui import Interface
from brain import QuizBrain
api_data = Data()
data = api_data.get_data()
quiz_brain = QuizBrain(data=data)
app_ui = Interface(quiz_brain)
