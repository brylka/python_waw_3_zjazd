import requests

url = 'https://api.frankfurter.dev/v1/latest?base=PLN'

response = requests.get(url)
data = response.json()

date = data['date']
rates = data['rates']
#print(rates)
#for key, value in rates.items():
#    print(f"{key} {value}")

pln = float(input("Ile masz pln: "))
euro = rates['EUR']*pln
print(f"Mając {pln}PLN możesz wymienić na {euro:.2f}EURO")
