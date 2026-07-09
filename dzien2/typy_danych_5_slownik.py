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

# nadpisanie
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 51}

dictionary['imie'] = ['Radek', 'Tomek', 'Magda']
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 51}

# wypisywanie
print(dictionary['wiek'])  # 51

# wypisac Tomek
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][1])  # Tomek
print(dictionary['imie'][1].lower())  # tomek
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

# print(dictionary['Imie'])  # KeyError: 'Imie'

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

print(chr(223))  # ß
print("\u00DF")  # ß

name1 = "GROSS"
name2 = "groß"

print(name1.lower() == name2.lower())  # False

"""Casefolding is similar to lowercasing but more aggressive because
 it is intended to remove all case distinctions in a string.
  For example, the German lowercase letter 'ß' is equivalent to "ss".
 Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss"."""
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"date": '12-12-2040'})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 51, 'date': '12-12-2040'}

dict_small = {'x': 20}
dict_small.update([("y", 3), ("z", 7)])
print(dict_small)  # {'x': 20, 'y': 3, 'z': 7}
