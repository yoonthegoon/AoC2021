# https://adventofcode.com/2021/day/2

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/2/input', cookies=dict(session=cookie))

commands = r.text.split('\n')[:-1]


def part1():
    h_pos, depth = 0, 0

    for command in commands:
        if 'forward' in command:
            h_pos += int(command[-1])
        elif 'down' in command:
            depth += int(command[-1])
        else:
            depth -= int(command[-1])

    return h_pos * depth


def part2():
    h_pos, depth, aim = 0, 0, 0

    for command in commands:
        if 'forward' in command:
            h_pos += int(command[-1])
            depth += aim * int(command[-1])
        elif 'down' in command:
            aim += int(command[-1])
        else:
            aim -= int(command[-1])

    return h_pos * depth


if __name__ == '__main__':
    print(part1())
    print(part2())
