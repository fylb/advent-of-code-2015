#!/usr/bin/env python3

import re
import itertools

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, to, wt):
        self.edges[to] = wt
        to.edges[self] = wt

    def dist_to(self, to):
        return self.edges[to]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Edge:
    # src - The source of an edge
    # to - destination of an edge
    # wt - distance between two nodes
    def __init__(self, a, b, w):
        self.src = a
        self.to = b
        self.wt = w



def first_pass():
    with open("input.txt") as lines:
        nodes = {}
        for line in lines.readlines():
            node_to_node = re.search("(\\w+) to (\\w+) = \\d+", line)
            nodes[node_to_node.group(1)] = Node(node_to_node.group(1))
            nodes[node_to_node.group(2)] = Node(node_to_node.group(2))

    with open("input.txt") as lines:
        for line in lines.readlines():
            node_to_node = re.search("(\\w+) to (\\w+) = (\\d+)", line)
            src = nodes[node_to_node.group(1)]
            to = nodes[node_to_node.group(2)]
            wt = int(node_to_node.group(3))
            src.add_edge(to, wt)

    print(list(nodes.values()))
    max_path = 2e9
    for comb in itertools.permutations(nodes.values()):
        current_cost = 0
        for i in range(len(comb) - 1):
            current_cost = current_cost + comb[i].dist_to(comb[i+1])
        print(f"Combination {comb} => {current_cost}")
        if current_cost < max_path:
            max_path = current_cost
    print(max_path)

def second_pass():
    with open("input.txt") as lines:
        nodes = {}
        for line in lines.readlines():
            node_to_node = re.search("(\\w+) to (\\w+) = \\d+", line)
            nodes[node_to_node.group(1)] = Node(node_to_node.group(1))
            nodes[node_to_node.group(2)] = Node(node_to_node.group(2))

    with open("input.txt") as lines:
        for line in lines.readlines():
            node_to_node = re.search("(\\w+) to (\\w+) = (\\d+)", line)
            src = nodes[node_to_node.group(1)]
            to = nodes[node_to_node.group(2)]
            wt = int(node_to_node.group(3))
            src.add_edge(to, wt)

    print(list(nodes.values()))
    max_path = 0
    for comb in itertools.permutations(nodes.values()):
        current_cost = 0
        for i in range(len(comb) - 1):
            current_cost = current_cost + comb[i].dist_to(comb[i+1])
        print(f"Combination {comb} => {current_cost}")
        if current_cost > max_path:
            max_path = current_cost
    print(max_path)


if __name__ == '__main__':
    second_pass()
