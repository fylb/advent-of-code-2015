#!/usr/bin/env python3

import re

input = "1113122113"

def first_pass():
    current_input = input
    for i in range(40):
        new_input = ''
        for group_of_numbers in [m.group(0) for m in re.finditer(r"(\d)\1*", current_input)]:
            new_input += f"{len(group_of_numbers)}{group_of_numbers[0]}"
        current_input = new_input
        print(len(current_input))

def second_pass():
    current_input = input
    for i in range(50):
        new_input = ''
        for group_of_numbers in [m.group(0) for m in re.finditer(r"(\d)\1*", current_input)]:
            new_input += f"{len(group_of_numbers)}{group_of_numbers[0]}"
        current_input = new_input
        print(len(current_input))


if __name__ == '__main__':
    #first_pass()
    second_pass()
