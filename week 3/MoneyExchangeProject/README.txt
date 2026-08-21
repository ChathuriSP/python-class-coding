Money Exchange System

Description :
This application developed to help a currency exchange business manage customers, currencies, exchange rates, and currency exchange transactions.

The system allows the business to:
Add Customers.
Store available currencies.
Manage currencies.
Manage exchange rates.
Perform currency exchanges.
Calculate the converted amounts.
Store completed exchange transactions.

The database is implemented using an OOP-style `Database` class.

Database Design:

This system contains 4 tables.
1.customers
2.currencies
3.exchange_rates
4.exchange_transactions

1.Customer table

This table stores information about customers who are using the money exchange service.
customer_id	-Primary Key
cus_name
phone
email

The 'customer_id' is used as a foreign key in the 'exchange_transactions' table.
This table is necessary to store customer information and identify which customer performs a currency exchange.

2.currencies table

This table stores the currecies supported by the money exchange business.
currency_id	-Primary Key
currency_code
currency_name
symbol

This table is necessary to maintain the list of currencies that can be exchanged by the business.
The 'currency_id' is used as a foreign key in the 'exchange_rates' and 'exchange_transactions' tables.

3.Exchange rates table

This table stores the exchange rates between different currencies.

rate_id		-Primary Key
rate
rate_date
to_currency_id		Foreign Key
from_currency_id	Foreign Key

The 'from_currency_id' and 'to_currency_id' are foreign keys connected to the 'currencies' table.

 
4.Exchange transactions table
This table stores every currency exchange performed by a customer.

transaction_id		-Primary Key
customer_id 		Foreign Key
from_currency_id 	Foreign Key
to_currency_id 		Foreign Key
amount
exchange_rate 		Foreign Key
converted_amount
transaction_date

This table is necessary to keep a record of every currency exchange performed by customers.
This table connects the customer, currencies, and exchange rate using foreign keys.
The 'from_currency_id' and 'to_currency_id' are foreign keys connected to the 'currencies' table.
The 'customer_id' is foreign keys connected to the 'customer' table.
The 'exchange_rate' is foreign keys connected to the 'exchange rate' table.

Database Relationships:
One customer can have many exchange transactions.
One currency can be used in many exchange rates.
Each exchange transaction belongs to one customer.
Each exchange transaction has one FROM currency and one TO currency.
One exchange rate can be used for many exchange transactions.

Main functions:

1.Add Customer

Allows the user to enter:

Customer name
Phone number
Email address

The information is stored in the customers table.

2. Perform Currency Exchange

The user can:

Enter a customer name.
Select a FROM currency.
Select a TO currency.
View the available exchange rate.
Enter the amount to exchange.
Calculate the converted amount.
Save the transaction.

After a successful exchange, the transaction is stored in the exchange_transactions table.

3.Exit
The user can exit the Money Exchange System by selecting the Exit option.



