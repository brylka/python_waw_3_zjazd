from flask import Flask, render_template, jsonify
import requests

url = 'https://api.frankfurter.dev/v1/latest?base=PLN'

response = requests.get(url)
data = response.json()
print(data)

city = {'Jelenia Góra': 100000, 'Warszawa': 345345345, 'Poznań': 324324}


app = Flask(__name__)

@app.route('/')
def hello():
    a = 'Witaj Flask!'
    return render_template("hello.html", hello=a)

@app.route('/trasa_z_bledem_500')
def error_500():
    return "Wystąpił błąd serwera", 500

@app.route('/api/kursy')
def api_kursy():
    return jsonify(data), 200

@app.route('/api/city')
def city():
    return jsonify(city)


if __name__ == '__main__':
    app.run(debug=True)