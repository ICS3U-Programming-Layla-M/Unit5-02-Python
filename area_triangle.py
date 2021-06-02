#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 2, 2021
# This program gets base and height from user and then calculates the area
# using functions (parameters, arguments)

def calc_area(base, height):
    # calculate and display the area
    area = (base * height) / 2
    print()
    print("The area of the triangle is: {:.2f}cm².". format(area))


def main():
    # greet user
    print("Today we will calculate the area of a triangle.")
    print()

    while True:
        # get the base
        base_string = input("Enter the base (cm): ")
        try:
            # convert form string to float
            base_float = float(base_string)
            if (base_float <= 0):
                # check if base is negative or 0
                print("{} is not a positive number, try again.\
". format(base_string))
            else:
                print()
                break
        except ValueError:
            # error message if input is not a number
            print("{} is not a number, try again.". format(base_string))

    while True:
        # get the height
        height_string = input("Enter the height (cm): ")
        try:
            # convert form string to float
            height_float = float(height_string)
            if (height_float <= 0):
                # check if height is negative or 0
                print("{} is not a positive number, try again.\
". format(height_string))
            else:
                break
        except ValueError:
            # error message if input is not a number
            print("{} is not a number, try again.". format(height_string))
    calc_area(base_float, height_float)


if __name__ == "__main__":
    main()
