# działąnia z plikami
# filehandler

# contex manager
# with - context manager w pythonie

# https://docs.python.org/3.14/library/functions.html#open
with open('test.log', "w", encoding='utf-8') as file:
    file.write("Powitanie\n")
    file.write("Jedno jeszcze\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', "x",  encoding='utf-8') as file:
#     file.write("Powitanie\n")
#     file.write("Jedno jeszcze\n")

with open('test.log', "w", encoding='utf-8') as file:
    file.write("Powitanie\n")
    file.write("Jedno jeszcze\n")

# dopisanie do pliku, na końcu
with open('test.log', "a", encoding='utf-8') as file:
    file.write("Dopisane\n")
    file.write("Dopisane 2\n")
    file.write("Dośdane\n")

with open('test.log', "r", encoding='utf-8') as fh:
    lines = fh.read()

print(lines)
