# REST API (ang. Representational State Transfer) to powszechny styl architektury oprogramowania,
# który pozwala aplikacjom komunikować się ze sobą przez protokół HTTP
# metody http
# GET: Pobieranie danych z serwera. Jest bezpieczna i idempotentna
# POST: Przesyłanie nowych danych do serwera (np. zawartości formularza), często w celu utworzenia nowego zasobu.
# PUT: Aktualizacja lub zastąpienie wskazanego zasobu nowymi danymi.
# PATCH: Częściowa modyfikacja zasobu.
# DELETE: Żądanie usunięcia określonego zasobu.
# https://github.com/public-apis/public-apis

import requests

# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - warningi, przekierowania
# 4xx - 404 brak strony, 400 Bad Request  - błedne dane
# 5xx - 500 internal Server Error

print(response.text)  # str

dane = response.json()
print(dane)
# {'table': 'A',
# 'currency': 'euro',
# 'code': 'EUR',
# 'rates': [{'no': '132/A/NBP/2026', 'effectiveDate': '2026-07-10', 'mid': 4.3465}]}
#
print(type(dane))  # <class 'dict'>

for k in dane:
    print(k)
# table
# currency
# code
# rates

# waluta, kurs
print("waluta:", dane['currency'])  # waluta: euro
print(dane['rates'])
# [
# {'no': '132/A/NBP/2026', 'effectiveDate': '2026-07-10', 'mid': 4.3465}
# ]
print(dane['rates'][0])
# {'no': '132/A/NBP/2026', 'effectiveDate': '2026-07-10', 'mid': 4.3465}
print("Kurs:", dane['rates'][0]['mid'])  # Kurs: 4.3465
