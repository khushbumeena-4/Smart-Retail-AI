import sqlite3

DB_NAME = "products.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            price REAL,
            quantity INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_product(name, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO products(name,price,quantity)
        VALUES(?,?,?)
    """, (name, price, quantity))

    conn.commit()
    conn.close()


def get_product(name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products WHERE name=?
    """, (name,))

    product = cursor.fetchone()

    conn.close()

    return product


def update_quantity(name, sold):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET quantity = quantity - ?
        WHERE name=?
    """, (sold, name))

    conn.commit()
    conn.close()


def get_all_products():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return products


if __name__ == "__main__":

    create_table()

    insert_product("Coke",40,100)
    insert_product("Pepsi",40,80)
    insert_product("Maggi",20,200)
    insert_product("Lays",20,150)
    insert_product("DairyMilk",50,120)
    insert_product("bottle",40,100)
    insert_product("banana",20,100)
    insert_product("apple",50,100)
    insert_product("orange",30,100)

    print("Database Created Successfully")