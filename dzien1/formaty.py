user = "Tomek"  # str
wiek = 39  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'>, zmiennoprzecinkowe

liczba = 9087654567891234321  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# %s - str
# %d - digit (liczba)

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
#
# TypeError: %d format: a real number is required, not str


print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3)  # Używamy wersji Pythona 3.00
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.1f" % 3.99)  # Używamy wersji Pythona 4.0
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 zaokrągli wyświetlanie
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4 zaokrągli wyświetlanie

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

print(wersja)  # 3.90001 nie zostałą zmieniona


