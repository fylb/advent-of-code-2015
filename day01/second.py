#!/usr/bin/env python3


def find_basement():
    with open('input.txt') as f:
        lines = f.readlines()[0]
        index = 0
        pos = 0
        while pos >= 0:
            if lines[index] == '(':
                pos += 1
            else:
                pos -= 1
            if pos < 0:
                print(index + 1)
                break
            index = index+1


if __name__ == '__main__':
    find_basement()
