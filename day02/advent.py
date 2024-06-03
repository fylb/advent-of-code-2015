#!/usr/bin/env python3


def first_part():
    with open("input.txt") as lines:
        boxes = [Box(dimension) for dimension in lines]
        print(sum([w.required_size() for w in boxes]))

def second_part():
    with open("input.txt") as lines:
        boxes = [Box(dimension) for dimension in lines]
        print(sum([w.ribbon_length() for w in boxes]))

class Box:
    def __init__(self, dimensions):
        measures = dimensions.split("x")
        self.h = int(measures[0])
        self.l = int(measures[1])
        self.w = int(measures[2])

    def wrapping_paper(self):
        return 2 * (self.h * self.w + self.h * self.l + self.w * self.l)

    def required_size(self):
        return self.wrapping_paper() + self.min_size()
    def min_size(self):
        return min(self.h * self.w,  self.h * self.l, self.w * self.l)

    def __str__(self):
        return f"{self.l} * {self.h} * {self.w} => {self.wrapping_paper()} + {self.min_size()}"

    def ribbon_length(self):
        lengths = [ self.h, self.l, self.w]
        min1 = min(lengths)
        lengths.remove(min1)
        min2 = min(lengths)
        return self.h * self.w * self.l + min1*2 + min2*2


if __name__ == '__main__':
    second_part()
    print(Box("2x3x4").ribbon_length())
    print(Box("1x1x10").ribbon_length())

