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


print(Human.__doc__)  # Klasa Human
# print(print.__doc__)
# pydoc -b
# pydoc -w kl1
