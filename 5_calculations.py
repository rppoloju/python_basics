# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to perform various calculations (addition, subtraction, multiplication, division and average calculation).
# Course: Python for Everybody
# Programming Assignment: Caculations
# Author: Rajendra Prasad Poloju
# Date: 09/28/2024
# ----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to perform various calculations
    Date of Change:09/28/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:09/28/2024
'''


# function to perform calculations (addition, subtraction, multiplication and division)
def perform_calculation(param_operation):
    #Prompt user to enter 2 numbers
    variable1 = int(input("Please input first number : "))
    variable2 = int(input("Please input second number : "))

    if param_operation == '+':
        outcome = variable1 + variable2
        print("The Addition of", variable1,"and",variable2,"is",outcome)
    elif param_operation == '-':
        outcome = variable1 - variable2
        print("The Subtraction of", variable1, "from", variable2, "is", outcome)
    elif param_operation == '*':
        outcome = variable1 * variable2
        print("The Multiplication of", variable1, "and", variable2, "is", outcome)
    elif param_operation == '/':
        outcome = variable1 / variable2
        print("The Division of", variable1, "by", variable2, "is", outcome)
    else:
        print("Operation is not valid")


# function to perform average of multiple numbers
def calculate_average():
    # Request user how many numbers average should be calculated.
    avg_count = int(input("Enter How many numbers do you want to average for? "))

    total = 0
    # For loop to request to enter numbers and calculate the sum of all numbers
    for i in range(avg_count):
        input_num = i+1
        user_num = int(input(f"Enter number {input_num}: "))
        total += user_num

    # Calculating the average
    average = total / avg_count
    print("The average of",avg_count, "numbers is:", average)


def main():
    while True:
        # Prompt user to enter the operation to perform
        user_operation = input("Enter the operation you want to perform (+ ,-, *,/, Avg) or Exit : ")

        if user_operation == 'Exit':
            break
        elif user_operation == 'Avg':
            calculate_average()
        else:
            perform_calculation(user_operation)


if __name__ == "__main__":
    main()

