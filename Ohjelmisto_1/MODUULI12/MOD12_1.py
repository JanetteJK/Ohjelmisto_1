#https://api.chucknorris.io/
import requests
import json

start = input("Press Enter for a Chuck Norris joke:\n")
ask = "https://api.chucknorris.io/jokes/random"
try:
    answer = requests.get(ask)
    if answer.status_code==200:
        json_answer = answer.json()
        print("Here's a joke:\n")
        print(json_answer["value"])
except requests.exceptions.RequestException as e:
    print ("Couldn't find page.")

