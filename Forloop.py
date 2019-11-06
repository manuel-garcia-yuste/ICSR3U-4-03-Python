#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program do a for loop


def main():
    # funciton calculates the number squared

    # variable
    answer = 1
    repeater = 0

    # input
    number = int(input("What is the number: "))

    # process
    for repeater in range(number + 1):
        answer = repeater * repeater
        print(str(repeater) + "² = " + str(answer))


if __name__ == "__main__":
    main()
