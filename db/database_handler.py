import sqlite3

from config.config_handler import config

create_set_table = """ CREATE TABLE IF NOT EXISTS sets (
                                        set_prefix text PRIMARY KEY,
                                        lang_first_occurence text,
                                        game_type text
                                    ); 
"""

insert_into_set_table = """INSERT INTO sets VALUE(%s, %s, %s)"""


def create_db():
    try:
        conn = sqlite3.connect(config.db_relative_path())
        cursor = conn.cursor()
        cursor.execute(create_set_table)
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


def add_set_entries(set_list):
    try:
        conn = sqlite3.connect(config.db_relative_path())
        cursor = conn.cursor()
        for entry in set_list:
            cursor.execute(insert_into_set_table % (entry['prefix'], entry['lang'], entry['type']))
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_db()
