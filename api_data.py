import requests


class Data:
    def __init__(self) -> None:
        self.parameters = {
            "amount": 10,
            "category": 18,
            "type": "boolean",
        }

    def get_data(self):
        response = requests.get("https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()
        data = response.json()["results"]
        return data
