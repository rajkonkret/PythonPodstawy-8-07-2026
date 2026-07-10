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