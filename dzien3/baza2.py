# baza danych - silnik
# relacyjne i nieralcyjne
# sql
# sqlite

import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')

    c = conn.cursor()
    print('Baza danych zostala podłaczona')

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
            """

    c.execute(query)
    conn.commit()

except sqlite3.Error as e:
    print("Bład:", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
# Baza danych zostala podłaczona
# Połaczenie zostało zamknięte
