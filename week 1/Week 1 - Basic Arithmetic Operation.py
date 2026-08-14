def main():
    # Ask user to enter two numbers
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")

    # Convert to float
    number1 = float(number1)
    number2 = float(number2)

    # Calculate Sum, Product, Subtraction and Division
    sum_value = number1 + number2
    subt_value = number1 - number2
    product_value = number1 * number2
    div_value = number1 / number2

    # Show the output
    print("Sum of the two numbers are: " + str(sum_value))
    print("Subtraction of the two numbers are: " + str(subt_value))
    print("Product of the two numbers are: " + str(product_value))
    print("Division of the two numbers are: " + str(div_value))


if __name__ == "__main__":
    main()