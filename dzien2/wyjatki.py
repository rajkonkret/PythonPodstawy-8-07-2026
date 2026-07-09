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
    int('A')  # ValueError: invalid literal for int() with base 10: 'A'
except ZeroDivisionError:
    print("Nie dziel przez zero")

print("Program działa nadal")
# Nie dziel przez zero
# Program działa nadal
#
# Process finished with exit code 0
