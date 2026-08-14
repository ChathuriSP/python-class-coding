class Bmi:
    def cal_bmi(self, weight, height):
        # Calculate BMI according to the standard formula
        self.bmi_value = float(weight) / (float(height) * float(height))

    def display(self):
        # Output the result
        print(f"Your body mass index (BMI) is: {round(self.bmi_value, 2)}")


def main():
    # input user's weight
    weight = input("Enter your weight (Kg): ")
    # input user's height
    height = input("Enter your height (m): ")

    # Call the class
    bmi = Bmi()
    bmi.cal_bmi(weight, height)
    bmi.display()


if __name__ == "__main__":
    main()