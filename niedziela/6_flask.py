from flask import Flask, render_template, jsonify, request
import requests

url = 'https://api.frankfurter.dev/v1/latest?base=PLN'

response = requests.get(url)
data = response.json()
print(data)

citys = {'Jelenia Góra': 100000, 'Warszawa': 345345345, 'Poznań': 324324}


app = Flask(__name__)

@app.route('/')
def hello():
    a = 'Witaj Flask!'
    return render_template("hello.html", hello=a)

@app.route('/trasa_z_bledem_500')
def error_500():
    return "Wystąpił błąd serwera", 500

@app.route('/kursy')
def kursy():
    return render_template("kursy.html", kursy=data['rates'])

@app.route('/przelicznik', methods=['GET', 'POST'])
def przelicznik():
    text = None
    if request.method == 'POST':
        pln = float(request.form['pln'])
        waluta = request.form['waluta']
        przelicznik = data['rates'][waluta]
        text = f"{pln}PLN = {pln*przelicznik}{waluta}"
    return render_template("przelicznik.html", kursy=data['rates'], text=text)




@app.route('/api/kursy')
def api_kursy():
    return jsonify(data), 200

@app.route('/api/city')
def city():
    return jsonify(citys), 200


if __name__ == '__main__':
    app.run(debug=True)