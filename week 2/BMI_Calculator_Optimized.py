def isfloat(n):
    """
    If string can be converted to floating number
    returns that number, otherwise returns false
    """
    try:
        return float(n);
    except ValueError:
        return False;


def inputfloat(hint):
    """
    Prints hint and asks to enter number.
    Repeats until decimal number is entered.
    """
    value = False
    while value is False:
        value = isfloat(input(hint))
        if value is False:
            print("Please enter number")
    return value


class BMIcalculator:
    def getdata(self):
        """
        Get weight in kgs and height in cms.
        Height is entered in cetimetres and stored in metres
        """

        self.w = inputfloat("Please enter your weight in kilograms:")
        self.h = inputfloat("Please enter your height in centimetres:") / 100

    def calculate(self):
        """
        Calculate and return bmi
        """

        return round(self.w / (self.h * self.h), 2)


def main():
    print("\n", "=" * 42, "\n")
    print("Hello, let's calculate your BMI.");

    calc = BMIcalculator()
    print()
    calc.getdata()
    bmi = calc.calculate()
    print(f"Your BMI is {bmi}")
    print("\n", "=" * 42, "\n")


if __name__ == "__main__":
    main()