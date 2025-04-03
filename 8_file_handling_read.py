# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to process a .txt file,
# calculate total words and
# output the number of occurrences of each word in the file.
# Course: Python for Everybody
# Programming Assignment: File Handling Read
# Author: Rajendra Prasad Poloju
# Date: 10/19/2024
# ----------------------------------------------------------------------------------------

'''
    Change#: 1
    Change(s) Made: Add logic to process a text file.
    Date of Change:10/19/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:10/19/2024
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


def main():
    param_dict ={} # dictionary to store words and counts
    gba_file = open('./gettysburg.txt','r')
    for line in gba_file:
        process_line(line,param_dict)
    pretty_print(param_dict)

if __name__ == "__main__":
    main()


