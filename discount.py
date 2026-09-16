from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-07-10

time = datetime.now()
print(time)  # 2026-07-10 10:23:04.810433

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

# formatowanie daty
formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 10/07/2026
print(type(formated_date))  # <class 'str'>

# 10:26 AM
# Dla czasu:
# %H: Godzina w formacie 24-godzinnym z zerem wiodącym, np. "00" do "23".
# %I: Godzina w formacie 12-godzinnym z zerem wiodącym, np. "01" do "12".
# %p: AM/PM.
# %M: Minuty z zerem wiodącym, np. "00" do "59".
# %S: Sekundy z zerem wiodącym, np. "00" do "59".
# %f: Mikrosekundy, np. "000000" do "999999".

formated_time = datetime.now().strftime("%I:%M %p")
print(formated_time)  # 10:29 AM
print(type(formated_time))

# zamiana obiekt
object_date = datetime.now().strptime("10/07/2026", "%d/%m/%Y")
print(object_date)  # 2026-07-10 00:00:00
print(type(object_date))  # <class 'datetime.datetime'>

#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-07-11

products = [
    {'sku': 1, "exp_date": today, "price": 200},
    {'sku': 2, "exp_date": today, "price": 100},
    {'sku': 3, "exp_date": tomorrow, "price": 50},
    {'sku': 4, "exp_date": today, "price": 200.00},
    {'sku': 5, "exp_date": today, "price": 1200},
    {'sku': 6, "exp_date": today, "price": 25.50},
]

for p in products:
    print(p)
    print(p['exp_date'])  # 2026-07-10

    if p['exp_date'] != today:
        continue

    p['price'] *= 0.8

    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f} pln""")
# {'sku': 6, 'exp_date': datetime.date(2026, 7, 10), 'price': 25.5}
# 2026-07-10
#
# Price for sku: 6
# is now: 20.40 pln
