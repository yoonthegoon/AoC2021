# https://adventofcode.com/2021/day/9

import math
import random
import requests
import sys

sys.setrecursionlimit(2000)

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/9/input', cookies=dict(session=cookie))

heightmap = r.text.split('\n')[:-1]


class Point:
    def __init__(self, x: int, y: int, height: int):
        self.x, self.y = x, y
        self.height = height
        self.visited = False
        self.north, self.south, self.east, self.west = 4*(None,)

    def neighbors(self):
        return [i for i in (self.north, self.south, self.east, self.west) if i]

    def risk(self):
        for neighbor in self.neighbors():
            if neighbor.height <= self.height:
                return 0
        return self.height + 1


class Heightmap:
    def __init__(self, h: list[str]):
        m = [[Point(x, y, int(p)) for x, p in enumerate(row)] for y, row in enumerate(h)]

        width, height = len(h[0]), len(h)
        for y, row in enumerate(h):
            for x, p in enumerate(row):
                if y - 1 in range(height):
                    m[y][x].north = m[y - 1][x]
                if y + 1 in range(height):
                    m[y][x].south = m[y + 1][x]
                if x + 1 in range(width):
                    m[y][x].east = m[y][x + 1]
                if x - 1 in range(width):
                    m[y][x].west = m[y][x - 1]

        self.map = m

    def risk(self):
        risk = 0
        for row in self.map:
            for p in row:
                risk += p.risk()
        return risk

    def basins(self):
        basins = []
        for row in self.map:
            for p in row:
                if p.risk():
                    basin = dfs(p.x, p.y, self, 0)
                    basins.append(basin)
        return basins


def dfs(current_x: int, current_y: int, h: Heightmap, size=0):
    current_p = h.map[current_y][current_x]
    current_p.visited = True
    size += 1

    while True:
        unvisited = [i for i in current_p.neighbors() if not i.visited and i.height < 9]
        if not unvisited:
            break

        next_p = random.choice(unvisited)

        size = dfs(next_p.x, next_p.y, h, size)

    return size


def part1():
    h = Heightmap(heightmap)
    return h.risk()


def part2():
    h = Heightmap(heightmap)
    return math.prod(sorted(h.basins(), reverse=True)[:3])


if __name__ == '__main__':
    print(part1())
    print(part2())
