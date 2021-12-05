# https://adventofcode.com/2021/day/5

import requests

cookie = open('.config', 'r').read()
# r = requests.get('https://adventofcode.com/2021/day/5/input', cookies=dict(session=cookie))
#
# lines = r.text.split('\n')[:-1]
lines = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]


class Vent:
    def __init__(self, line):
        coords1, coords2 = line.split(' -> ')
        self.x1, self.y1 = (int(i) for i in coords1.split(','))
        self.x2, self.y2 = (int(i) for i in coords2.split(','))

    def orientation(self):
        if self.x1 == self.x2:
            return 'vertical'
        elif self.y1 == self.y2:
            return 'horizontal'
        else:
            return 'diagonal'


class Field:
    def __init__(self):
        self.field = [10*[0, ] for _ in range(10)]

    def draw(self, vent: Vent):
        if vent.orientation() == 'vertical':
            if vent.y2 > vent.y1:
                for i in range(vent.y1, vent.y2 + 1):
                    self.field[i][vent.x1] += 1
            else:
                for i in range(vent.y2, vent.y1 + 1):
                    self.field[i][vent.x1] += 1
        elif vent.orientation() == 'horizontal':
            if vent.x2 > vent.x1:
                for i in range(vent.x1, vent.x2 + 1):
                    self.field[vent.y1][i] += 1
            else:
                for i in range(vent.x2, vent.x1 + 1):
                    self.field[vent.y1][i] += 1
        else:
            if vent.y2 > vent.y1:
                if vent.x2 > vent.x1:
                    for x, y in zip(range(vent.x1, vent.x2 + 1), range(vent.y1, vent.y2 + 1)):
                        self.field[y][x] += 1
                else:
                    for x, y in zip(range(vent.x2, vent.x1 + 1), range(vent.y1, vent.y2 + 1)):
                        self.field[y][x] += 1
            else:
                if vent.x2 > vent.x1:
                    for x, y in zip(range(vent.x1, vent.x2 + 1), range(vent.y2, vent.y1 + 1)):
                        self.field[y][x] += 1
                else:
                    for x, y in zip(range(vent.x2, vent.x1 + 1), range(vent.y2, vent.y1 + 1)):
                        self.field[y][x] += 1

    def overlaps(self):
        count = 0
        for row in self.field:
            for val in row:
                if val > 1:
                    count += 1
        return count


def part1():
    field = Field()

    for line in lines:
        vent = Vent(line)
        field.draw(vent)

    for f in field.field:
        print(''.join(str(i if i else '.') for i in f))

    return field.overlaps()


def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
