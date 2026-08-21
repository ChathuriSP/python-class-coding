from user_manager import (
    database,
    add_customer,
    add_sample_customers,
    add_sample_currencies,
    add_sample_exchange_rates,
    perform_exchange
)


def main():

    # Create database tables
    database.create_tables()

    # Add sample data
    add_sample_customers()
    add_sample_currencies()
    add_sample_exchange_rates()

    while True:
        print("----------------------------------------")
        print("       MONEY EXCHANGE SYSTEM")
        print("----------------------------------------")
        print("1. Add Customer")
        print("2. Perform Currency Exchange")
        print("3. Exit")
        print("-----------------------------------------")

        choice = input("Enter your choice: ").strip()

        # Add Customer

        if choice == "1":
            print("\n--- Add Customer ---")
            cus_name = input("Enter customer name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()

            if not cus_name or not phone or not email:
                print("All customer fields are required.")
                continue
            add_customer(cus_name,phone,email)

        # Currency Exchange
        elif choice == "2":
            perform_exchange()

        # Exit

        elif choice == "3":
            print("\nThank you for using Money Exchange System.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()