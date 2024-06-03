#!/usr/bin/env python3


def count_parentheses():
    with open('input.txt') as f:
        lines = f.readlines()[0]
        open_parentheses = len([c for c in lines if c == '('])
        close_parentheses = len([c for c in lines if c == ')'])
        print(open_parentheses-close_parentheses)


if __name__ == '__main__':
    count_parentheses()