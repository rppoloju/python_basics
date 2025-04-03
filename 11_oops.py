# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to create a Simple Cash Program Using OOP Concepts.
# Course: Python for Everybody
# Programming Assignment: OOP Concepts
# Author: Rajendra Prasad Poloju
# Date: 11/09/2024
# ----------------------------------------------------------------------------------------

"""
    Change#: 1
    Change(s) Made: Create a Simple Cash Program .
    Date of Change:11/09/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:11/09/2024
"""

import locale

locale.setlocale(locale.LC_ALL, '')


class CashRegister:
    def __init__(self):
        self.total_price = 0.0
        self.item_count = 0

    def add_item(self,price):
        self.total_price += price
        self.item_count += 1

    def get_total_price(self):
        return self.total_price

    def get_item_count(self):
        return self.item_count


def main():
    # Display a welcome message for user.
    print("Welcome to Ameya Cash Register!")

    cash_register = CashRegister()
    while True:
        try:
            user_price = input("Please enter item price (or enter 'X' to exit): ")
            if user_price.lower() == "x":
                break
            else:
                user_price = float(user_price)
                cash_register.add_item(user_price)
        except ValueError:
            print("Please enter valid item price.")

    print(f"Total Number of items in cart: {cash_register.get_item_count()}")
    print(f"Total $ amount of the cart: {locale.currency(cash_register.get_total_price(), grouping=True)}")


if __name__ == "__main__":
    main()
