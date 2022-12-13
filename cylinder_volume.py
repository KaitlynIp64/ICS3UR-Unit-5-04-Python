#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius: int, height: int) -> float:
    # calculate volume
    volume = math.pi * radius**2 * height
    return volume


def main():
    # input
    print("This program calculates the volume of a cylinder.")
    str_radius = input("Enter the radius of the cylinder (cm): ")
    str_height = input("Enter the height of the cylinder (cm): ")

    try:
        radius = int(str_radius)
        height = int(str_height)
        # call functions
        total_volume = calculate_volume(radius, height)
        print(
            "The volume of a cylinder with a radius of {0}cm and a height of {1}cm is {2}cm³.".format(
                radius, height, round(total_volume, 2)
            )
        )
    except ValueError:
        print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
