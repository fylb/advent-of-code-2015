#!/usr/bin/env python3

import re


class Wire:
    def __init__(self, id, line):
        self.id = id
        self.value = 0
        self.line = line
        self.sources = []

    def __str__(self):
        return f"{self.id} (from {self.line})"

    @staticmethod
    def init_from_line(line):
        id = line[line.find('-> ') + 3:].strip()
        return Wire(id, line.strip())

    def compute(self, wires):
        if self.value > 0:
            return self.value
        assignment = re.search(r"^(\w+) -> ", self.line)
        if assignment:
            source = assignment.group(1)
            if source.isnumeric():
                print(f"It's a raw assignment from {source} ({self.line})")
                self.value = int(source)
            else:
                print(f"It's an assignment from {source} ({self.line})")
                self.value = wires.wires[source].compute(wires)

        not_action = re.search(r"^NOT (.*) -> ", self.line)
        if not_action:
            source = not_action.group(1)
            if source.isnumeric():
                print(f"It's a raw NOT on {source} ({self.line})")
                self.value =  65536 + ~ int(source)
            else:
                print(f"It's NOT on {source} ({self.line})")
                self.value =  65536 + ~ wires.wires[source].compute(wires)

        or_action = re.search(r"^(.*) OR (.*) -> ", self.line)
        if or_action:
            source1 = or_action.group(1)
            source2 = or_action.group(2)
            print(f"It's an OR on {source1} / {source2} ({self.line})")
            if source1.isnumeric():
                src1 = int(source1)
            else:
                src1 = wires.wires[source1].compute(wires)
            if source2.isnumeric():
                src2 = int(source2)
            else:
                src2 = wires.wires[source2].compute(wires)
            self.value =  src1 | src2

        and_action = re.search(r"^(.*) AND (.*) -> ", self.line)
        if and_action:
            source1 = and_action.group(1)
            source2 = and_action.group(2)
            print(f"It's an AND on {source1} / {source2} ({self.line})")
            if source1.isnumeric():
                src1 = int(source1)
            else:
                src1 = wires.wires[source1].compute(wires)
            if source2.isnumeric():
                src2 = int(source2)
            else:
                src2 = wires.wires[source2].compute(wires)
            self.value =  src1 & src2

        rshift_action = re.search(r"^(.*) RSHIFT (.*) -> ", self.line)
        if rshift_action:
            source = rshift_action.group(1)
            shift = int(rshift_action.group(2))
            print(f"It's an RSHIFT on {source} by  {shift} ({self.line})")
            if source.isnumeric():
                src = int(source)
            else:
                src = wires.wires[source].compute(wires)
            self.value =  src >> shift

        lshift_action = re.search(r"^(.*) LSHIFT (.*) -> ", self.line)
        if lshift_action:
            source = lshift_action.group(1)
            shift = int(lshift_action.group(2))
            print(f"It's an LSHIFT on {source} by  {shift} ({self.line})")
            if source.isnumeric():
                src = int(source)
            else:
                src = wires.wires[source].compute(wires)
            self.value = src << shift

        return self.value


class Wires:
    def __init__(self):
        self.wires = dict()

def first_pass():
    with open("input.txt") as lines:
        wires = Wires()
        for l in lines.readlines():
            wire = Wire.init_from_line(l)
            wires.wires[wire.id] = wire
        print(wires.wires['a'])
        print(wires.wires['a'].compute(wires))

def second_pass():
    with open("input.txt") as lines:
        wires = Wires()
        for l in lines.readlines():
            wire = Wire.init_from_line(l)
            wires.wires[wire.id] = wire
        print(wires.wires['a'])
        b_value = wires.wires['a'].compute(wires)
        for k,v in wires.wires.items():
            v.value = 0
        wires.wires['b'].value = b_value
        print(wires.wires['a'].compute(wires))

if __name__ == '__main__':
    # first_pass()
    second_pass()
