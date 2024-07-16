
import requests

url = 'https://open.er-api.com/v6/latest/TRY'
response = requests.get(url)

data = response.json()
rates = data['rates']


usd = rates['USD']
eur = rates['EUR']
gel = rates['GEL']
rub = rates['RUB']


print(f"1 Turk lirasi ")
print((f"{usd:} USD") )

# print(f"{eur:} EUR")
print(f"{gel:} GEL")
print(f"{rub:} RUB")