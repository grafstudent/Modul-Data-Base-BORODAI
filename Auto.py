import sqlite3

b = sqlite3.connect('autosalon.db')
cursor = b.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        color TEXT NOT NULL DEFAULT "Black",
        year INTEGER NOT NULL)''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_id INTEGER,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (car_id) REFERENCES cars(id))''')
b.commit()

def insert_car(brand, model, color, year):
    cursor.execute('INSERT INTO cars (brand, model, color, year) VALUES (?, ?, ?, ?)', (brand, model, color, year))
    b.commit()

def insert_part(car_id, name, price):
    cursor.execute('INSERT INTO parts (car_id, name, price) VALUES (?, ?, ?)', (car_id, name, price))
    b.commit()
def display_cars():
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    if cars:
        print("Cars:")
        for car in cars:
            print(car)
    else:
        print("No cars found.")

def display_parts():
    cursor.execute('SELECT * FROM parts')
    parts= cursor.fetchall()
    for part in parts:
        print(part)

def display_cars_by_color(color):
    cursor.execute('''SELECT * FROM cars WHERE color = ? ''', (color,))
    cars = cursor.fetchall()
    if not cars:
        print(f"No cars found with color '{color}'.")
    else:
        print("Cars:")
        for car in cars:
            print(car)


def display_parts_by_model(car_id):
    cursor.execute('''SELECT cars.brand, parts.* FROM parts JOIN cars ON parts.car_id = cars.id WHERE cars.id = ?''', (car_id,))
    parts = cursor.fetchall()
    if not parts:
        print(f"No parts found for cars with car_id '{car_id}'.")
    else:
        print("Parts:")
        for part in parts:
            print(part)

def delete_cars(id):
    cursor.execute('DELETE FROM cars WHERE id = ?', (id,))
    b.commit()

def delete_parts(id):
    cursor.execute('DELETE FROM parts WHERE id = ?', (id,))
    b.commit()


# Додавання запису в таблицю cars
#insert_car('Toyota', 'Camry', 'Blue', 2021)

# Додавання запису в таблицю parts
#insert_part(4, 'Air Filter', 150.0)


# Виведення всіх записів з таблиці cars
#display_cars()

# Виведення всіх записів з таблиці parts
#display_parts()

# Виведення та фільтрація машин за кольором
#display_cars_by_color('Red')

# Виведення та фільтрація запчастин за id_car
#display_parts_by_model(2)

b.close()