# klasa -  przepis
#  obiekt - zbudowany wg klasy
# hermetyzacja, dziedziczenie , polimorfizm i abstrakcja

# CamelCase
class Human:
    """
    Klasa Human
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizująca
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def wypisz_imie(self):
        print(f"Mam na imię: {self.imie}")


print(Human.__doc__)  # Klasa Human
# print(print.__doc__)
# pydoc -b
# pydoc -w kl1

cz1 = Human("Radek", 69, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

#
# Radek
# 69
# m
cz1.wypisz_imie()
# Mam na imię: Radek

cz2 = Human("Anna", 23)
cz2.wypisz_imie()


# Mam na imię: Anna

# dziedziczenie
class Student(Human):
    """
    Dziedziczy po klasie Human
    """

    def wypisz_oceny(self):
        print("Moje oceny: 5, 5, 6")


stud1 = Student("Tomek", 27, "m")
stud1.wypisz_imie()  # Mam na imię: Tomek
stud1.wypisz_oceny()  # Moje oceny: 5, 5, 6
