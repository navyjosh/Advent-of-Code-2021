from settings import *


def read_input():
    input_file = os.path.join(INPUT_PATH, 'day2.txt')
    measurements = open(input_file, 'r').readlines()
    return measurements


def sol1(movements):
    pos = 0
    depth = 0
    for m in movements:
        direction, units = m.split()
        units = int(units)
        if direction == "forward":
            pos += units
        elif direction == "up":
            depth -= units
        elif direction == "down":
            depth += units
        else:
            print(direction, units)
    return depth * pos


def sol2(movements):
    pos = 0
    depth = 0
    aim = 0
    for m in movements:
        direction, units = m.split()
        units = int(units)
        if direction == "forward":
            pos += units
            depth += aim * units
        elif direction == "up":
            aim -= units
        elif direction == "down":
            aim += units
        else:
            print(direction, units)
    return depth * pos


if __name__ == "__main__":
    moves = read_input()
    solution1 = sol1(moves)
    solution2 = sol2(moves)
    print("solution 1:", solution1)
    print("solution 2:", solution2)
