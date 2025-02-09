import requests


data= requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean" ,verify=False)
data=data.json()
question_data=data['results']

