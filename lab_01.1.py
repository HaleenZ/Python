import datetime

def calculate_year_to_100(age):
    current_year = datetime.datetime.now().year
    year_to_100 = current_year + (100 - age)
    return year_to_100

def greet_and_calculate():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    year_to_100 = calculate_year_to_100(age)
    print("Hello, " + name + "! You will turn 100 years old in the year " + str(year_to_100) + ".")

greet_and_calculate()
