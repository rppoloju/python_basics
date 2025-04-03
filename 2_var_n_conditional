#---------------------------------------------------------------------------------------
# Purpose of Program: This is to calculate total installation cost of fiber optic cable
# Course: Python for Everybody
# Programming Assignment: Variables and Conditional Statements
# Author: Rajendra Prasad Poloju
# Date: 09/06/2024
#----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to calculate total installation cost
    Date of Change:09/06/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/06/2024
'''

#Display a welcome message for your user.
print("Welcome!!! This is your Fiber Optic Cable cost calculator")

#Retrieve the company name from the user.
user_company_name = input("Please enter your company name here : ") 

#Retrieve the number of feet of fiber optic cable to be installed from the user.
user_cable_length = int(input("Please enter fiber optic cable length to be installed in feet : "))
feet_or_foot = "feet"
if user_cable_length == 1:
    feet_or_foot = "foot"


#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
cable_cost_per_foot = 0.87
cable_total_cost = user_cable_length * cable_cost_per_foot

#Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost i.e. total cost in a legible format.
print("---------------Receipt-----------------")
print("Company Name:",user_company_name)
print("Fiber Optic Cable Length to be Installed:",user_cable_length,feet_or_foot)
print("Total Installation Cost: $",cable_total_cost)
print("---------------Receipt-----------------")