# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to work on list of temperatures.
# Course: Python for Everybody
# Programming Assignment: List and Dictionaries
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
    text ='My Name is Rajendra. I am a data Scientist. I can build data science solutions'
    counts = {}
    for word in text.split():
        counts.setdefault(word, 0)  # If the word isn't in the dictionary, set it to 0
        counts[word] += 1  # Add 1 to the count
    print(counts)
    a = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 2, 2]
    unq_list = list(dict.fromkeys(a))
    print(unq_list)
    telephone = {'mike': '402-555-1212', 'barb': '314-231-8973', 'andy': '515-643-9087'}
    print(telephone.get('alan'))

    telephone1 = {'mike': '402-555-1212'}
    telephone2 = {'barb': '314-231-8973', 'andy': '515-643-9087'}
    telephone = telephone1 | telephone2
    print(telephone)

    name = input("Enter a name: ")

    result = {
    "mike": f"Mike's phone number is {telephone['mike']}",
    "barb": f"Barb's phone number is {telephone['barb']}",
    "andy": f"Andy's phone number is {telephone['andy']}"
    }.get(name, "Name not found")
    print(result)


if __name__ == "__main__":
    main()


