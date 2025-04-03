# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to invoke chuck norris API to get random jokes.
# Course: Python for Everybody
# Programming Assignment: API's
# Author: Rajendra Prasad Poloju
# Date: 11/02/2024
# ----------------------------------------------------------------------------------------

"""
    Change#: 1
    Change(s) Made: Add logic to process a text file.
    Date of Change:11/02/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:11/02/2024
"""
# pip install requests
import requests


def get_chuck_norris_joke():
    try:
        url = "https://api.chucknorris.io/jokes/random"
        querystring = {"category": "travel"}
        api_headers = {'cache-control': "no-cache"}
        apiresponse = requests.request("GET", url, headers=api_headers, params=querystring)
        json_response = apiresponse.json()
        return f"Chuck Norris Joke: {json_response['value']}"
    except (requests.exceptions.RequestException,KeyError) as exp:
        return "There are No Chuck Norris Jokes available at this time."


def main():
    # Display a welcome message for your user.
    print("Welcome to Chuck Norris Random Jokes!")
    while True:
        print(get_chuck_norris_joke())
        # Prompt user if user want another joke
        user_input = input("if you want another joke, Type 'Y' or 'y' ")
        if user_input.lower() == "y":
            continue
        else:
            print("Thank you for using Chuck Norris Random Jokes.")
            break


if __name__ == "__main__":
    main()
