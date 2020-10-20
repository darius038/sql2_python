from database import DatabaseContextManager

def alter_table_customer():
    query = """ALTER TABLE CUSTOMER 
    ADD CONSTRAINT UNIQUE emails customers_table """
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS CUSTOMER(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    email TEXT UNIQUE,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES COMPANY(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_company():
    query = """CREATE TABLE IF NOT EXISTS COMPANY(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT UNIQUE,
    employee_count INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# ------------------------Customer CRUD------------------------

# Create function
def create_customer(first_name: str, last_name: str, age: int, email: str, company_id: int):
    query = """INSERT INTO CUSTOMER(first_name, last_name, age, email, company_id) VALUES(?,?,?,?,?)"""
    parameters = [first_name, last_name, age, email, company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

# Read function
def get_customer():
    query = """SELECT * FROM CUSTOMER"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

# Update function
def update_customer(first_name: str, last_name: str, new_age: int):
    query = """UPDATE CUSTOMER
                SET  age = ?,
                WHERE first_name = ? , last_name = ? """
    parameters = [new_age, first_name, last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

# Delete function
def delete_customer(customer_id: int):
    query = """DELETE FROM CUSTOMER
               WHERE id = ?"""
    parameters = [customer_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

# ------------------------Company CRUD------------------------
def create_company(company_name: str, employee_count: int):
    query = """INSERT INTO COMPANY(company_name, employee_count) VALUES(?, ?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def get_company():
    query = """SELECT * FROM COMPANY"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)

def update_company(company_name: str, new_employee_count: int):
    query = """UPDATE COMPANY
                SET employee_count = ?
                WHERE company_name = ?"""
    parameters = [new_employee_count, company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_company(company_id: int):
    query = """DELETE FROM COMPANY
                WHERE company_id = ?"""
    parameters = [company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_company_customer():
    query = """SELECT * FROM CUSTOMER
                JOIN COMPANY
                    ON Customer.company_id = Company.company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_table():
    query = """DROP TABLE CUSTOMER"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def drop_table_company():
    query = """DROP TABLE COMPANY"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

# drop_table()
# drop_table_company()
# alter_table_customer()
# create_table_company()
# create_company("imone1", 123456)
# create_company("imone2", 123658)
# get_company()
# create_table_customer()
# create_customer("Darius", "Pav", 44, "dar@mail.com", 1)
# get_customer()
# get_company_customer()