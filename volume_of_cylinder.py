#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: Nov 2019
# This program uses user defined functions
# To calculate volume of a cylinder

import math


def volume_cylinder(h, r):
    # calculate cylinder

    # process
    volume = (r**2) * math.pi * h

    # output
    return volume


def main():
    # This checks if input is an integer and positive,
    # then calls function

    # Input
    input_1 = input("Enter the radius of the cylinder(cm): ")
    input_2 = input("Enter the height of the cylinder(cm): ")
    print("")
    try:
        radius_cylinder = int(input_1)
        height_cylinder = int(input_2)
        if (radius_cylinder > 0 and height_cylinder > 0):
            # call functions
            volume = volume_cylinder(r=radius_cylinder,
                                     h=height_cylinder)
            print("The volume of the cylinder is: {0:,.2f}cm^3".format(volume))
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
