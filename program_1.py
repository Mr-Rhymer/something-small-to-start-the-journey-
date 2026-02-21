# The year you turned 100 years old
name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    current_year = 2026
    year_turn_100 = current_year + (100 - age)
    print(f"Hello {name}, you will turn 100 in the year {year_turn_100}.")
except ValueError:
    print("Please enter a valid integer for your age.")