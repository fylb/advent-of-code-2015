#!/usr/bin/env python3

def count_chars_1(s):
    p = s.strip()[1:-1]
    count = 0
    i = 0
    while i < len(p):
        print(f"testing {p[i]} of {p[i:]}")
        if p[i] == '\\' and p[i + 1] == 'x':
            print(f"=> \\x bidule")
            i = i + 4
        elif p[i] == '\\' and p[i + 1] == '\\':
            print(f"=> \\ ")
            i = i + 2
        elif p[i] == '\\' and p[i + 1] == '"':
            print(f"=> \" ")
            i = i + 2
        else:
            i = i + 1
        count = count + 1
    return len(s.strip()), count


def count_chars_2(s):
    p = s.strip()[1:-1]
    count = 6
    i = 0
    while i < len(p):
        print(f"testing {p[i]} of {p[i:]}")
        if p[i] == '\\' and p[i + 1] == 'x':
            i = i + 4
            count = count + 5
        elif p[i] == '\\' and p[i + 1] == '\\':
            print(f"=> \\ ")
            i = i + 2
            count = count + 4
        elif p[i] == '\\' and p[i + 1] == '"':
            print(f"=> \" ")
            i = i + 2
            count = count + 4
        else:
            i = i + 1
            count = count + 1
    return len(s.strip()), count


def first_pass():
    with open("input.txt") as lines:
        total_number_of_code_literals = 0
        total_number_of_code_memory = 0
        for line in lines.readlines():
            l, m = count_chars_1(line)
            print(f"{line.strip()} => {l}, {m}")
            total_number_of_code_literals += l
            total_number_of_code_memory += m
        print(total_number_of_code_literals-total_number_of_code_memory)

def second_pass():
    with open("input.txt") as lines:
        total_number_of_code_literals = 0
        total_number_of_code_memory = 0
        for line in lines.readlines():
            l, m = count_chars_2(line)
            print(f"{line.strip()} => {l}, {m}")
            total_number_of_code_literals += l
            total_number_of_code_memory += m
        print(total_number_of_code_literals-total_number_of_code_memory)

if __name__ == '__main__':
    # first_pass()
    second_pass()
    print(count_chars_2('"abc"'))
    print(count_chars_2('"aaa\\"aaa"'))
    print(count_chars_2('"\\x27"'))
