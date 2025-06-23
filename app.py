from flask import Flask, render_template, request, jsonify
import requests
import csv
import os

app = Flask(__name__)

CSV_FILE = 'kursy_walut.csv'
NBP_API_URL = 'http://api.nbp.pl/api/exchangerates/tables/C?format=json'

def fetch_and_save_rates():
    response = requests.get(NBP_API_URL)
    if response.status_code == 200:
        data = response.json()[0]['rates']
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['currency', 'code', 'bid', 'ask'], delimiter=';')
            writer.writeheader()
            writer.writerows(data)
        return True
    return False

def load_rates_from_csv():
    rates = {}
    if not os.path.exists(CSV_FILE):
        fetch_and_save_rates()

    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            rates[row['code']] = float(row['ask'])
    return rates

@app.route('/')
def index():
    rates = load_rates_from_csv()
    return render_template('kalkulator.html', rates=rates)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    code = data.get('currency')
    amount = float(data.get('amount', 0))
    rates = load_rates_from_csv()
    if code not in rates:
        return jsonify({'error': 'Nieznany kod waluty'}), 400
    result = round(amount * rates[code], 2)
    return jsonify({'result': result})

@app.route('/update')
def update():
    success = fetch_and_save_rates()
    return "Zaktualizowano dane." if success else "Błąd pobierania danych."

if __name__ == '__main__':
    app.run(debug=True)