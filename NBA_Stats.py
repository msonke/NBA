import http.client
from secrets import secrets

conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

secret_key = secrets.get('SECRET_KEY')

headers = {
    'X-RapidAPI-Key': secret_key,
    'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }

conn.request("GET", "/stats?page=0&per_page=25", headers=headers)

res = conn.getresponse()
data = res.read()

with open("[stats].json", "w") as file:
    file.write(data.decode('utf-8'))
