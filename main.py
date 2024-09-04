from api_data import Data
from ui import Ui
api_data = Data()
data = api_data.get_data()
quiz_category = data[0]["category"]
ui = Ui(quiz_category=quiz_category)
