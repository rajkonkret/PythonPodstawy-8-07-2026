# słownik - para klucz : wartosc
# {"user" : "Radek"}
# klucze nie mogą sie powtarzac
# {"name":"John", "age":30, "car":null}
# słownik jest odpowiednikiem jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz 'wiek'
dictionary['wiek'] = 51
print(dictionary)  # {'imie': 'Radek', 'wiek': 51}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 51])
# dict_items([('imie', 'Radek'), ('wiek', 51)])