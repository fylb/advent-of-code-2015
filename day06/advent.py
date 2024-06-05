#!/usr/bin/env python3

import re


class LightGrid:
    def __init__(self):
        self.grid = [
            [False for i in range(1000)] for i in range(1000)
        ]
        self.brightness = [
            [0 for i in range(1000)] for i in range(1000)
        ]

    def instruction(self, data):
        result = re.search(r"^(.*) (\d+),(\d+) through (\d+),(\d+)", data)
        action = result.group(1)
        start_x = int(result.group(2))
        start_y = int(result.group(3))
        end_x = int(result.group(4)) + 1
        end_y = int(result.group(5)) + 1
        match action:
            case "turn off":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.grid[x][y] = False
            case "turn on":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.grid[x][y] = True
            case "toggle":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.grid[x][y] = not self.grid[x][y]

    def count_lit(self):
        c = 0
        for line in self.grid:
            for column in line:
                if column:
                    c += 1
        return c

    def instruction_brightness(self, data):
        result = re.search(r"^(.*) (\d+),(\d+) through (\d+),(\d+)", data)
        action = result.group(1)
        start_x = int(result.group(2))
        start_y = int(result.group(3))
        end_x = int(result.group(4)) + 1
        end_y = int(result.group(5)) + 1
        match action:
            case "turn off":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.brightness[x][y] = max(0, self.brightness[x][y]-1)
            case "turn on":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.brightness[x][y] += 1
            case "toggle":
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        self.brightness[x][y] += 2

    def total_brightness(self):
        c = 0
        for line in self.brightness:
            for column in line:
                c += column
        return c

    def __str__(self):
        return repr(self.grid)


def first_pass():
    with open("input.txt") as lines:
        grid = LightGrid()
        for l in lines.readlines():
            grid.instruction(l)
        print(grid.count_lit())

def second_pass():
    with open("input.txt") as lines:
        grid = LightGrid()
        for l in lines.readlines():
            grid.instruction_brightness(l)
        print(grid.total_brightness())

if __name__ == '__main__':
    # first_pass()
    second_pass()
