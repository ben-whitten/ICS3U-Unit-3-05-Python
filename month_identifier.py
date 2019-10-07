#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you the name of the month you input.


def main():
    # This is what tells you the name of the month you input.

    # Input
    number_of_month = int(input("Input the number of a month (1-12): "))

    # Process
    if number_of_month == 1:
        # Output
        print("")
        print("January")
    # Process
    elif number_of_month == 2:
        # Output
        print("")
        print("February")
    # Process
    elif number_of_month == 3:
        # Output
        print("")
        print("March")
    # Process
    elif number_of_month == 4:
        # Output
        print("")
        print("April")
    # Process
    elif number_of_month == 5:
        # Output
        print("")
        print("May")
    # Process
    elif number_of_month == 6:
        # Output
        print("")
        print("June")
    # Process
    elif number_of_month == 7:
        # Output
        print("")
        print("July")
    # Process
    elif number_of_month == 8:
        # Output
        print("")
        print("August")
    # Process
    elif number_of_month == 9:
        # Output
        print("")
        print("September")
    # Process
    elif number_of_month == 10:
        # Output
        print("")
        print("October")
    # Process
    elif number_of_month == 11:
        # Output
        print("")
        print("November")
    # Process
    elif number_of_month == 12:
        # Output
        print("")
        print("December")
    # Process
    elif number_of_month > 12:
        # Output
        print("")
        print("Thats not a month")
    # Process
    elif number_of_month < 1:
        # Output
        print("")
        print("Thats not a month")
    # Process
    else:
        # It is impossible to get here because of the int(input) so if you do
        # here you most likely did something wrong.
        print("Error, check you number and try again.")


if __name__ == "__main__":
    main()
