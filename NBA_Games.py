import http.client
import json
from secrets import secrets


conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

secret_key = secrets.get('SECRET_KEY')

headers = {
    'X-RapidAPI-Key': secret_key,
    'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }

conn.request("GET", "/games?page=0&per_page=25", headers=headers)

res = conn.getresponse()
data = res.read()

with open("[games].json", "w") as file:
    file.write(data.decode('utf-8'))

