import csv

data = [{
    "table": "C",
    "no": "071/C/NBP/2020",
    "tradingDate": "2020-04-09",
    "effectiveDate": "2020-04-10",
    "rates": [
        {"currency": "dolar amerykański", "code": "USD", "bid": 4.1117, "ask": 4.1947},
        {"currency": "dolar australijski", "code": "AUD", "bid": 2.5907, "ask": 2.6431},
        {"currency": "dolar kanadyjski", "code": "CAD", "bid": 2.9388, "ask": 2.9982},
        {"currency": "euro", "code": "EUR", "bid": 4.4945, "ask": 4.5853},
        {"currency": "frank szwajcarski", "code": "CHF", "bid": 4.2487, "ask": 4.3345},
        {"currency": "funt szterling", "code": "GBP", "bid": 5.1287, "ask": 5.2323}
    ]
}]

rates = data[0]['rates']

with open('kursy_walut.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['currency', 'code', 'bid', 'ask'], delimiter=';')
    writer.writeheader()
    writer.writerows(rates)

print("Plik CSV został zapisany.")
