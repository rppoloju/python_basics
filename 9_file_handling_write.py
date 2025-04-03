# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to process a .txt file,
# calculate total words and
# output the number of occurrences of each word to a user specified file.
# Course: Python for Everybody
# Programming Assignment: File Handling Write
# Author: Rajendra Prasad Poloju
# Date: 10/26/2024
# ----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to process a text file.
    Date of Change:10/19/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:10/19/2024

    Change#: 2
    Change(s) Made: Modified the program to write output toa file.
    Date of Change:10/26/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:10/26/2024
'''


# function to add each word to the dictionary
def add_word(param_word,param_dict):
    param_word = param_word.lower()
    if param_word in param_dict:
        param_dict[param_word] += 1
    else:
        param_dict[param_word] = 1


# function to process each line, split out the words
def process_line(line,param_dict):
    replace_char = (',', '--', '.',"-")
    for each_repl_char in replace_char:
        line = line.replace(each_repl_char, ' ')
    param_words= line.split()
    for param_word in param_words:
        add_word(param_word,param_dict)


# function to print sorted words based on occurrences
def pretty_print(param_dict):
    print("Length of the dictionary:", len(param_dict))
    print(f"{'Word':<20}{'Count'}")
    print("-" * 27)
    sorted_words = sorted(param_dict.items(), key=lambda val: (val[1],val[0]), reverse=True)
    for word, count in sorted_words:
        print(f"{word:<22}{count}")


#function to write output to a file.
def process_file(param_dict, user_filename):
    with open(user_filename, 'a') as user_file:
        sorted_words = sorted(param_dict.items(), key=lambda val: (val[1], val[0]), reverse=True)
        for word, count in sorted_words:
            user_file.write(f"{word:<22}{count}\n")


def main():
    param_dict ={} # dictionary to store words and counts
    gba_file = open('./gettysburg.txt','r')
    for line in gba_file:
        process_line(line,param_dict)
    #pretty_print(param_dict)
    user_filename = input("Please enter the file name: ")
    with open(user_filename, 'w') as user_file:
        user_file.write(f"Length of the dictionary: {len(param_dict)}\n")
        user_file.write(f"{'Word':<20}{'Count'}\n")
        user_file.write("-" * 27 + "\n")
    process_file(param_dict,user_filename)


if __name__ == "__main__":
    main()


