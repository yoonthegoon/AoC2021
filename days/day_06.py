# https://adventofcode.com/2021/day/6

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/6/input', cookies=dict(session=cookie))

population = [int(i) for i in r.text.replace('\n', '').split(',')]


def part1():
    pop = population.copy()

    for _ in range(80):
        for i, fish in enumerate(pop):
            if not fish:
                pop[i] = 6
                pop.append(9)
            else:
                pop[i] -= 1

    return len(pop)


def part2():
    pop = [0]*9
    for i in population:
        pop[i] += 1

    for _ in range(256):
        pop.append(pop[0])
        pop[7] += pop[0]
        pop.pop(0)

    return sum(pop)


if __name__ == '__main__':
    print(part1())
    print(part2())
