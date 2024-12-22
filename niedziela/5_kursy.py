import requests

url = 'https://api.frankfurter.dev/v1/latest?base=PLN'

response = requests.get(url)
data = response.json()

print(response.status_code)

if response.status_code == 200:
    print(data)
else:
    print("coś jest nie tak")

