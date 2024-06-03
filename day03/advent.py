#!/usr/bin/env python3

def first_part():
    with open("input.txt") as f:
        moves = f.readlines()[0]
        visit = Visit()
        for m in moves:
            visit.move(m)
        print(len(visit.visited))

def second_part():
    with open("input.txt") as f:
        moves = f.readlines()[0]
        visit = Visit()
        for m in moves:
            visit.move_with_robot(m)
        print(len(visit.visited))

class Visit:
    def __init__(self):
        self.current_position = 0, 0
        self.current_position_robot = 0, 0
        self.visited = dict()
        self.visited[self.current_position] = 1
        self.robot_move = False

    def move(self, movement):
        match movement:
            case '>':
                self.current_position = self.current_position[0], self.current_position[1] + 1
            case '<':
                self.current_position = self.current_position[0], self.current_position[1] - 1
            case '^':
                self.current_position = self.current_position[0] + 1, self.current_position[1]
            case 'v':
                self.current_position = self.current_position[0] - 1, self.current_position[1]
        if self.current_position in self.visited:
            self.visited[self.current_position] += 1
        else:
            self.visited[self.current_position] = 1

    def move_with_robot(self, movement):
        cur_pos_robot = self.current_position_robot
        cur_pos = self.current_position
        if self.robot_move:
            match movement:
                case '>':
                    self.current_position_robot = self.current_position_robot[0], self.current_position_robot[1] + 1
                case '<':
                    self.current_position_robot = self.current_position_robot[0], self.current_position_robot[1] - 1
                case '^':
                    self.current_position_robot = self.current_position_robot[0] + 1, self.current_position_robot[1]
                case 'v':
                    self.current_position_robot = self.current_position_robot[0] - 1, self.current_position_robot[1]
            if self.current_position_robot in self.visited:
                self.visited[self.current_position_robot] += 1
            else:
                self.visited[self.current_position_robot] = 1
            self.robot_move = False
        else:
            self.move(movement)
            self.robot_move = True

        print(f"{movement} {self.robot_move} : {cur_pos} => {self.current_position}, {cur_pos_robot} => {self.current_position_robot}")


if __name__ == '__main__':
    #first_part()
    second_part()
