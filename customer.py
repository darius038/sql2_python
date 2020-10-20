import sqlite3


# -------------------Context Manager-------------------
class DatabaseContextManager(object):
    """This class exists for us to use less lines of code than necessary for queries.
        __init__: used to set database file name.
        __enter__: opens connection and creates cursor.
        __exit__: commits the changes to database file and closes connection."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


# ------------------------Table Creation------------------------
# This is the first thing you have to do before creating any record in the database.
# Without Tables your database won't work as it is a template for the information/data that you're trying to create
def create_customer_table():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    age INTEGER,)"""
    with DatabaseContextManager("CRUD") as db:
        db.execute(query)


# ------------------------CRUD------------------------
# CRUD stands for Create, Read, Update, Delete
# Create or in SQL INSERT is used to create new records in the database.
# Read(get) or in SQL SELECT is used to read data from the database
# Update is used to update data for already existing record
# Delete for deleting records that are already created.

# Create function
def create_customer(first_name, last_name, address, age):
    query = f"""INSERT INTO Books(title, author, pages, library_id) VALUES(?,?,?,?)"""
    # Question marks are used in initial query to have placeholders for upcoming parameters.
    # (This is used to protect ourselves from SQL Injection attacks)
    parameters = [title, author, pages, library_id]
    # Parameters are used to pass values that were given when calling the function.
    with DatabaseContextManager("db") as db:
        db.execute(sql=query, parameters=parameters)
        # We can pass sql and parameters to execute method which will set our values by order from parameters array or touple


# Read function
def get_books():
    query = """SELECT * FROM Books"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function
def update_customer(first_name, last_name, age):
    query = """UPDATE Customer
                SET age = ?
                WHERE title = ?"""
    parameters = [new_title, old_title]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Delete function
def delete_book(title: str):
    query = """DELETE FROM Books
                WHERE title = ?"""
    parameters = [title]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# ------------------------Library CRUD------------------------
def create_library(name: str, address: str):
    query = """INSERT INTO Library(name, address) VALUES(?, ?)"""
    parameters = [name, address]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_libraries():
    query = """SELECT * FROM Library"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_library_name(old_name: str, new_name: str):
    query = """UPDATE Library
                SET name = ?
                WHERE name = ?"""
    parameters = [new_name, old_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_library(name: str):
    query = """DELETE FROM Library
                WHERE name = ?"""
    parameters = [name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_books_libraries():
    query = """SELECT * FROM Books
                JOIN Library
                    ON Books.library_id = Library.library_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_table():
    query = """DROP TABLE Library"""
    with DatabaseContextManager("db") as db:
        db.execute(query)