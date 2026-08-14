class TempConverter:
    
    def __init__(self, temp):
        self.temp = temp

    def to_celsius(self):
        #Convert Fahrenheit to Celsius
        return (self.temp - 32) * 5 / 9

    def to_fahrenheit(self):
        #Convert Celsius to Fahrenheit
        return (self.temp * 9 / 5) + 32

    def convert(self, user_input):
        #Determine the conversion direction based on user input
        if user_input == 'F':
            return self.to_celsius()
        elif user_input == 'C':
            return self.to_fahrenheit()
        else:
            raise ValueError("Invalid input. Please enter the temperature with the 'C' or 'F' prefix.")


def main():
    #Main function to run the temperature converter
    user_input = input("Enter temperature(eg, F51 or C11): ").strip().upper()

    try:
        # Check that the input has at least two characters
        if len(user_input) < 2:
            raise ValueError(
                "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."
            )
        input_value = user_input[0]

        temp = float(user_input[1:])

        converter = TempConverter(temp)

        # conversion
        result = converter.convert(input_value)

        if user_input == 'F':
            print(f"{temp}°F is converted to {result:.2f}°C")
        else:
            print(f"{temp}°C is converted to {result:.2f}°F")

    except ValueError as error:
        print(error)


# Execute the main function
if __name__ == "__main__":
    main()