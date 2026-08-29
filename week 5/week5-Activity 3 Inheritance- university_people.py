class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

    def describe(self):
        return "Person({}, {})".format(self.name, self.address)
    def display_details (self):
        print("Name :", self.name)
        print("Address :", self.address)
        print("Age :", self.age)
        print("ID :", self.id)

class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        super().__init__(name, address, age, id)
        self.academic_record = academic_record
    def display_student_details(self):
        self.display_details()
        print("Academic Record :", self.academic_record)

class AcademicStaff(Person):
    def __init__(self, name, address, age, id, tax_code, salary, publications):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code
        self.salary = salary
        self.publications = publications

    def calculate_publications(self):
        return len (self.publications)

    def display_academicstaff_details(self):
        self.display_details()
        print("Tax Code :", self.tax_code)
        print("Salary :", self.salary)
        print("Number of Publications :", self.calculate_publications())

class GeneralStaff(Person):
    def __init__(self, name, address, age, id, tax_code, pay_rate):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def calculate_payrate(self):
        return self.pay_rate

    def display_generalstaff_details(self):
        self.display_details()
        print("Tax Code :", self.tax_code)
        print("Pay Rate :", self.calculate_payrate())

 #Add Student details
student = Student("Chathuri Perera", "Auckland, New Zealand", 35, "S001", "Master of software Engineering - A Grade")

 #Add Academic staff details
academicstaff = AcademicStaff("Dr. Chathura Rajapaksha", "Auckland, New Zealand", 59,"A001","T0025","$95000",
                              ["Artificial Intelligence Research",
                               "Data Mining Research",
                               "Bigdata Analytics Research"])
# Add General staff details
generalstaff = GeneralStaff ("Sayuni Jayasuriya", "Auckland, New Zealand", 25, "G001", "TA001",30)

# Display Student details
print("==============Student Details==================")
student.display_student_details()

# Display Academic Staff details
print("==============Academic Staff Details==================")
academicstaff.display_academicstaff_details()

# Display General Staff details
print("==============General Staff Details==================")
generalstaff.display_generalstaff_details()

