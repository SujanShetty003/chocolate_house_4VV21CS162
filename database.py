import sqlite3

def connect_db():
    conn = sqlite3.connect('chocolate_house.db') ###  Eatablish a connection to the SQlite database , returns: Sqlite3.connection: An SQlite connectionm object for the 'chocolate_house.db' database

    return conn

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY,
            flavor_name TEXT NOT NULL,
            availability TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY,
            ingerdent_name TEXT NOT NULL,
            quantity INTEGER
        ) 
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS cuastomer_suggestions (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                flavor_suggestion Text,
                allergy_concern TEXT
            )
        ''')
    conn.commit()
    conn.close()