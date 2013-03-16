#!/usr/bin/env python
import sqlite3
from names import FILES


DATABASE = 'names.db'


def create_tables(cursor):
    cursor.execute("CREATE TABLE first_names (name, gender, cumm_prob)")
    cursor.execute("CREATE INDEX first_names_index on first_names(cumm_prob)")
    cursor.execute("CREATE TABLE last_names (name, cumm_prob)")
    cursor.execute("CREATE INDEX last_names_index on last_names(cumm_prob)")


def populate_last_names(cursor):
    with open(FILES['last']) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            cursor.execute("INSERT INTO last_names VALUES (?, ?)", (
                name.capitalize(), float(cummulative)))


def populate_first_names(cursor, gender):
    with open(FILES['first:%s' % gender]) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            cursor.execute("INSERT INTO first_names VALUES (?, ?, ?)", (
                name.capitalize(), gender, float(cummulative)))


if __name__ == "__main__":
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        create_tables(cursor)
        populate_first_names(cursor, 'female')
        populate_first_names(cursor, 'male')
        populate_last_names(cursor)
