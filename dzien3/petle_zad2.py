dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for v in dictionary.items():
    print(v)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, v, sep=" <==> ")
# imie <==> Radek
# nazwisko <==> Kowalski