from api_data import Data
from ui import Ui
api_data = Data()
data = api_data.get_data()
quiz_category = data[0]["category"]
quiz_question = {data[0]["question"]: data[0]["correct_answer"]}
ui = Ui(quiz_category=quiz_category, quiz_question=quiz_question)
