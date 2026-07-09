# wyjątki - błedy podczas wykonywania programu

# print(0 / 1)
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-8-07-2026\dzien2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

try:
    # print(5 / 0)
    # int('A')  # ValueError: invalid literal for int() with base 10: 'A'
    # print(2 + "A")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # raise KeyError("Bład klucza")
    wynik = 20 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład:", e)
else:  # wykona się tylko gdy nie ma błedu
    print("wynik:", wynik)
finally:  # wykona się zawsze
    print("kolejne obliczenie")
    print(50 * "-")

# try, except [else, finally]
print("Program działa nadal")
# Nie dziel przez zero
# Program działa nadal
#
# Process finished with exit code 0
# Bład: 'Bład klucza'
# Program działa nadal
