from database_money_exchange import Database


# Create Database object
database = Database()

# add customer

def add_customer(cus_name, phone, email):
    conn = database.create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO customers (cus_name, phone, email) VALUES (?, ?, ?)
        """, (cus_name, phone, email))
        conn.commit()
        print("Customer added successfully.")
    except Exception as e:
        print("Error adding customer:", e)
    finally:
        conn.close()

#add sample customers
def add_sample_customers():
    conn = database.create_connection()
    cursor = conn.cursor()

    customers = [
        ("Chathuri", "0226006568", "chathura@gmail.com"),
        ("Vikum", "0226186369", "viki123@gmail.com"),
        ("Sayuni", "0225639856", "sayu234@gmail.com")
    ]

    try:
        cursor.executemany("""
            INSERT INTO customers (cus_name, phone, email) VALUES (?, ?, ?)
        """, customers)

        conn.commit()
        print("customers added successfully.")

    except Exception as e:
        print("Error adding customers:", e)

    finally:
        conn.close()

# Add Currency

def add_currency(currency_code, currency_name, symbol):
    conn = database.create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO currencies (currency_code, currency_name, symbol) VALUES (?, ?, ?)
        """, (currency_code, currency_name, symbol))

        conn.commit()
        print("Currency added successfully.")

    except Exception as e:
        print("Error adding currency:", e)

    finally:
        conn.close()

#add sample currencies
def add_sample_currencies():
    conn = database.create_connection()
    cursor = conn.cursor()

    currencies = [
        ("USD", "US Dollar", "$"),
        ("NZD", "New Zealand Dollar", "$"),
        ("LKR", "Sri Lankan Rupee", "Rs."),
        ("INR", "Indian Rupee", "Rs.")
    ]

    try:
        cursor.executemany("""
            INSERT INTO currencies (currency_code, currency_name, symbol) VALUES (?, ?, ?)
        """, currencies)

        conn.commit()
        print("Currencies added successfully.")

    except Exception as e:
        print("Error adding currencies:", e)

    finally:
        conn.close()


# Add Exchange rates

def add_exchange_rate(rate, from_currency_id, to_currency_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO exchange_rates (rate, from_currency_id, to_currency_id) VALUES (?, ?, ?)
        """, (rate, from_currency_id, to_currency_id))

        conn.commit()
        print("Exchange rate added successfully.")

    except Exception as e:
        print("Error adding exchange rate:", e)

    finally:
        conn.close()

#add sample exchange rate
def add_sample_exchange_rates():
    conn = database.create_connection()
    cursor = conn.cursor()

    exchange_rates = [
        (1.68, "USD", "NZD"),
        (0.60, "NZD", "USD"),
        (330.33, "USD", "LKR"),
        (0.0030, "LKR", "USD"),
        (3.45, "INR", "LKR"),
        (0.29, "LKR", "INR"),
        (95.73, "USD", "INR"),
        (0.010, "INR", "USD"),
        (197.27, "NZD", "LKR"),
        (0.0051, "LKR", "NZD"),
        (57.15, "NZD", "INR"),
        (0.017, "INR", "NZD")
    ]

    try:

        for rate, from_code, to_code in exchange_rates:

            # Get From Currency ID
            cursor.execute("""
                SELECT currency_id FROM currencies WHERE UPPER(currency_code) = UPPER(?)
            """, (from_code,))

            from_currency = cursor.fetchone()

            # Get To Currency ID
            cursor.execute("""
                SELECT currency_id FROM currencies WHERE UPPER(currency_code) = UPPER(?)
            """, (to_code,))

            to_currency = cursor.fetchone()

            if from_currency and to_currency:

                # Check whether rate already exists
                cursor.execute("""
                               SELECT rate_id
                               FROM exchange_rates
                               WHERE rate = ?
                                 AND from_currency_id = ?
                                 AND to_currency_id = ?
                               """, (
                                   rate,
                                   from_currency[0],
                                   to_currency[0]
                               ))

                existing_rate = cursor.fetchone()

                if not existing_rate:
                    cursor.execute("""
                        INSERT INTO exchange_rates (rate, from_currency_id, to_currency_id)
                            VALUES (?, ?, ?)
                            """, (rate,from_currency[0],to_currency[0]))

        conn.commit()
        print("Exchange rates added successfully.")

    except Exception as e:
        print("Error adding exchange rates:", e)

    finally:
        conn.close()

# Display Available Currencies

def display_currencies():
    conn = database.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT currency_id, currency_code, currency_name, symbol FROM currencies ORDER BY currency_id
    """)
    currencies = cursor.fetchall()
    conn.close()

    print("\nAvailable Currencies")
    print("-" * 25)

    for currency in currencies:

        print(f"{currency[0]}. " f"{currency[1]} - " f"{currency[2]} ({currency[3]})" )
    print("-" * 25)

# Find Customer

def find_customer(customer_name):
    conn = database.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id, cus_name FROM customers WHERE LOWER(cus_name) = LOWER(?)
    """, (customer_name,))

    customer = cursor.fetchone()
    conn.close()
    return customer

# Get Currency ID

def get_currency_id(currency_code):

    conn = database.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT currency_id FROM currencies WHERE UPPER(currency_code) = UPPER(?)
    """, (currency_code,))

    currency = cursor.fetchone()
    conn.close()

    if currency:
        return currency[0]

    return None

# GET CURRENT EXCHANGE RATE

def get_exchange_rate(from_currency_id, to_currency_id):

    conn = database.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT rate_id,rate FROM exchange_rates WHERE from_currency_id = ? AND to_currency_id = ?
        ORDER BY rate_date DESC LIMIT 1
    """, (from_currency_id,to_currency_id))

    exchange_rate = cursor.fetchone()
    conn.close()
    return exchange_rate

# Display Currency Exchange

def perform_exchange():

    print("\n")
    print("=" * 25)
    print("  Money Exchange System")
    print("=" * 25)
# request customer name
    customer_name = input("Enter customer name: ").strip()

    customer = find_customer(customer_name)
    if not customer:
        print("\nCustomer not found.")
        print("Please add the customer before making an exchange.")
        return

    customer_id = customer[0]
    print(f"\nCustomer: {customer[1]}")

    display_currencies()

#Enter currency details

    from_code = input( "\nEnter FROM currency code: " ).strip().upper()
    from_currency_id = get_currency_id(from_code)
    if not from_currency_id:
        print("Invalid FROM currency.")
        return


    to_code = input( "Enter TO currency code: " ).strip().upper()
    to_currency_id = get_currency_id(to_code)
    if not to_currency_id:
        print("Invalid TO currency.")
        return

    # currency check whether the from currency and to currencies are same.

    if from_currency_id == to_currency_id:
        print("FROM and TO currencies cannot be the same.")
        return

    # Get exchange rate


    exchange_rate_data = get_exchange_rate(from_currency_id,to_currency_id)

    if not exchange_rate_data:
        print(f"\nNo exchange rate available for "f"{from_code} -> {to_code}")
        return

    rate_id = exchange_rate_data[0]
    exchange_rate = exchange_rate_data[1]

    # Display exchange rate

    print("\n")
    print(f"Exchange Rate: 1 {from_code} = "f"{exchange_rate} {to_code}")


    # request to enter amount
    try:
        amount = float(input(f"Enter amount in {from_code}: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    # Calculate converted amount
    converted_amount = amount * exchange_rate
    print("\n")
    print("-" * 30)
    print("EXCHANGE SUMMARY")
    print("-" * 30)

    print(f"Customer          : {customer[1]}")
    print(f"From Currency     : {from_code}")
    print(f"To Currency       : {to_code}")
    print(f"Amount            : {amount:.2f} {from_code}")
    print(f"Exchange Rate     : {exchange_rate}")
    print(f"Converted Amount  : "f"{converted_amount:.2f} {to_code}")
    print("-" * 25)

    # Save transaction details

    conn = database.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO exchange_transactions(
                customer_id,exchange_rate_id,from_currency_id,to_currency_id,amount,exchange_rate,converted_amount)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (customer_id,rate_id,from_currency_id,to_currency_id,amount,exchange_rate,converted_amount))
        conn.commit()

        print("\nTransaction saved successfully!")
    except Exception as e:
        print("\nError saving transaction:", e)
    finally:
        conn.close()