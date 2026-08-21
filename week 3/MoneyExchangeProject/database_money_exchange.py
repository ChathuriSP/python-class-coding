import sqlite3


class Database:

    def __init__(self, database_name="moneyexchange.db"):
        self.database_name = database_name

    def create_connection(self):
        conn = sqlite3.connect(self.database_name)

        # Enable foreign key support in SQLite
        conn.execute("PRAGMA foreign_keys = ON")

        return conn

    def create_tables(self):

        conn = self.create_connection()
        cursor = conn.cursor()

        # Customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cus_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')


        # Currencies table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS currencies (
                currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                currency_code TEXT NOT NULL UNIQUE,
                currency_name TEXT NOT NULL,
                symbol TEXT NOT NULL
            )
        ''')

        # Exchange rates table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exchange_rates (
                rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                rate REAL NOT NULL,
                rate_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                to_currency_id INTEGER NOT NULL,
                from_currency_id INTEGER NOT NULL,
                FOREIGN KEY (to_currency_id) REFERENCES currencies(currency_id),
                FOREIGN KEY (from_currency_id) REFERENCES currencies(currency_id)
            )
        ''')


        # Exchange transactions table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exchange_transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                exchange_rate_id INTEGER NOT NULL,
                from_currency_id INTEGER NOT NULL,
                to_currency_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                exchange_rate REAL NOT NULL,
                converted_amount REAL NOT NULL,
                transaction_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id)REFERENCES customers(customer_id),
                FOREIGN KEY (exchange_rate_id) REFERENCES exchange_rates(rate_id),
                FOREIGN KEY (from_currency_id) REFERENCES currencies(currency_id),
                FOREIGN KEY (to_currency_id) REFERENCES currencies(currency_id)
            )
        ''')

        conn.commit()
        conn.close()

        print("All tables created successfully!")