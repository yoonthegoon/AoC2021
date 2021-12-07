# https://adventofcode.com/2021/day/7

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/7/input', cookies=dict(session=cookie))

h_pos_lst = [int(i) for i in r.text.replace('\n', '').split(',')]


def part1():
    return int(sum(map(lambda h_pos: abs(h_pos - sorted(h_pos_lst)[len(h_pos_lst)//2]), h_pos_lst)) + .5)


def part2():
    return int(sum(map(lambda h_pos: (lambda a: a*(a + 1)/2)(abs(h_pos - int(sum(h_pos_lst)/len(h_pos_lst)))), h_pos_lst)) + .5)


if __name__ == '__main__':
    print(part1())
    print(part2())
