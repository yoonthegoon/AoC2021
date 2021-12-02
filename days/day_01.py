# https://adventofcode.com/2021/day/1

import requests

cookie = open('.config', 'r').read()
s = requests.session()
r = s.get('https://adventofcode.com/2021/day/1/input', cookies=dict(session=cookie))

depths = [int(i) for i in r.text.split('\n')[:-1]]


def measurements(lst: list) -> list:
    return ['increased' if lst[i] > lst[i - 1] else 'decreased' for i in range(1, len(lst))]


def part1():
    return measurements(depths).count('increased')


def part2():
    sums = [depths[i] + depths[i - 1] + depths[i - 2] for i in range(2, len(depths))]
    return measurements(sums).count('increased')


if __name__ == '__main__':
    print(part1())
    print(part2())
