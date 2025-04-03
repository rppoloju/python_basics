# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to work on list of temperatures.
# Course: Python for Everybody
# Programming Assignment: Loops
# Author: Rajendra Prasad Poloju
# Date: 10/05/2024
# ----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to ask user temperatures and find max & Min
    Date of Change:10/05/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:10/05/2024
'''


def main():
    #Create an empty list called temperatures.
    temperatures = [] #no elements
    while True:  # Allow the user to input a series of temperatures
        # Prompt user to enter the temperatures
        user_temperature = input("Enter a valid temperature value (or Type 'Done') : ")
        if user_temperature.lower() == 'done':  # a sentinel value which will stop the user input.
            break
        else:
            try:
                user_temp = float(user_temperature)
                temperatures.append(user_temp)
            except ValueError:
                print("Invalid Temperature. Please enter a Valid Temperature.")

    if not temperatures:
        print("No Valid Temperatures entered")
    else:
        user_max_temperature=max(temperatures)
        user_min_temperature=min(temperatures)

        print("Total Number of Temperatures Entered:",len(temperatures))
        print("Largest Temperature Entered:",user_max_temperature)
        print("Smallest Temperature Entered:",user_min_temperature)


if __name__ == "__main__":
    main()


