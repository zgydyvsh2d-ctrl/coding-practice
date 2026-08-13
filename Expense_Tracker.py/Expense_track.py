# TRACK-CALCULATE-DISPLAY
import sys


def display_screen():
    print("=== Monthly Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("4. Quit ")
    user_choice = input("SELECT OPTION or PRESS 'Q' TO QUIT:")


def add_expense():
    Expense = input("Enter your expense:")
    category = input("Enter your category")
    price = input("Enter your price")
    print(Expense)


# Take Input and store in collection
quit_program = True
if quit_program is False:
    print("Goodbye!")
    sys.exit()
else:
    display_screen()
