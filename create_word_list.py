# testes para ir pro main
import requests
from datetime import datetime
import pandas as pd

word_list = []

print(datetime.now())

for i in range(500):
    data = requests.get("https://random-words-api.vercel.app/word")
    word = data.json()[0]['word']
    word_list.append(word)

df = pd.DataFrame(word_list, columns=['words'])
df.to_csv('word_list.csv', index=False)

print(datetime.now())