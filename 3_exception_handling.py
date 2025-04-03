# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to calculate total installation cost of fiber optic cable
# Course: Python for Everybody
# Programming Assignment: Exception Handling
# Author: Rajendra Prasad Poloju
# Date: 09/13/2024
# ----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to calculate total installation cost
    Date of Change:09/06/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/06/2024

    Change#: 2
    Change(s) Made: Added Exception handling if Invalid Total feet is entered by the user
    Date of Change:09/13/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/13/2024

    Change#: 3
    Change(s) Made: Changed Total Cost Calculation Logic to include discounted price per foot
    Date of Change:09/13/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/13/2024

    Change#: 4
    Change(s) Made: formatted the cost amount to retain 2 decimal values
    Date of Change:09/13/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/13/2024

'''

# Display a welcome message for your user.
print("Welcome!!! This is your Fiber Optic Cable cost calculator")

# Retrieve the company name from the user.
user_company_name = input("Please enter your company name here : ") 

# Retrieve the number of feet of fiber optic cable to be installed from the user.
user_cable_length = 0
try:
    user_cable_length = int(input("Please enter fiber optic cable length to be installed in feet : "))
except ValueError:
    print("Fiber Optic Cable Length entered is not Valid. Please enter a valid length in feet.")
else:
    if user_cable_length<=0:
        print("Fiber Optic Cable Length entered must be more than 0. Please enter a valid length in feet.")
    else:
        feet_or_foot = "feet"
        if user_cable_length == 1:
            feet_or_foot = "foot"

        # Calculate the installation cost of fiber optic cable by multiplying the no of feet with the discounted price.
        # if number of feet entered is more than 500 then cable cost per foot is $0.50.
        # if number of feet entered is more than 250 then cable cost per foot is $0.70.
        # if number of feet entered is more than 100 then cable cost per foot is $0.80.
        # default cable cost per foot is $0.87.

        cable_cost_per_foot = 0.87
        if user_cable_length>500:
            cable_cost_per_foot = 0.50
        elif user_cable_length>250:
            cable_cost_per_foot = 0.70
        elif user_cable_length>100:
            cable_cost_per_foot = 0.80

        cable_total_cost = float(user_cable_length * cable_cost_per_foot)

        # Print a receipt for the user including the company name, number of feet of fiber to be installed and
        # the calculated cost i.e. total cost in a legible format.
        print("---------------Receipt-----------------")
        print("Company Name:",user_company_name)
        print("Fiber Optic Cable Length to be Installed:",user_cable_length,feet_or_foot)
        print("Fiber Optic Cable Cost per foot: ${:.2f}".format(cable_cost_per_foot))
        print("Total Installation Cost: ${:.2f}".format(cable_total_cost))
        print("---------------Receipt-----------------")
finally:
    print("Thanks You for Using Fiber Optic Cable cost calculator!")


