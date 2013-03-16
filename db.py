import sqlite3
import random


DATABASE = 'names.db'


def fetch_first_name(cursor, selected, gender):
    cursor.execute("SELECT name from first_names WHERE gender = ? AND "
        "cumm_prob > ? ORDER BY cumm_prob", (gender, selected))
    return cursor.fetchone()[0]


def fetch_last_name(cursor, selected):
    cursor.execute("SELECT name from last_names WHERE cumm_prob > ? "
            "ORDER BY cumm_prob", (selected,))
    return cursor.fetchone()[0]


def get_full_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    first_num, last_num = random.random() * 90, random.random() * 90
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        first_name = fetch_first_name(cursor, first_num, gender)
        last_name = fetch_last_name(cursor, last_num)
    return u"%s %s" % (first_name, last_name)
