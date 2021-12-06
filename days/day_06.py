# https://adventofcode.com/2021/day/6

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/6/input', cookies=dict(session=cookie))

# population = [int(i) for i in r.text.replace('\n', '').split(',')]
# population = [3, 4, 3, 1, 2]
population = [6]


def part1():
    pop1 = population.copy()

    for _ in range(80):
        for i, fish in enumerate(pop1):
            if not fish:
                pop1[i] = 6
                pop1.append(9)
            else:
                pop1[i] -= 1

    return len(pop1)


def part2():
    pop2 = population.copy()

    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
