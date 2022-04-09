# https://adventofcode.com/2021/day/8

import re
import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/8/input', cookies=dict(session=cookie))

notes = r.text.split('\n')[:-1]


def part1():
    count = 0
    for entry in notes:
        keys, values = entry.split(' | ')
        for value in values.split(' '):
            if len(value) in (2, 3, 4, 7):
                count += 1
    return count


def part2():
    zero, one, two, three, four, five, six, seven, eight, nine = 10*('',)

    count = 0
    for entry in notes:

        group_five = []
        group_six = []

        keys, values = entry.split(' | ')
        for key in keys.split(' '):
            key = ''.join(sorted(key))
            match len(key):
                case 2:
                    one = key
                case 3:
                    seven = key
                case 4:
                    four = key
                case 5:
                    group_five.append(key)
                case 6:
                    group_six.append(key)
                case 7:
                    eight = key

        for i in group_five:
            if len(re.findall(f'[{one}]', i)) == 2:
                three = i
            elif len(re.findall(f'[{four}]', i)) == 2:
                two = i
            else:
                five = i

        for i in group_six:
            if len(re.findall(f'[{three}]', i)) == 5:
                nine = i
            elif len(re.findall(f'[{one}]', i)) == 2:
                zero = i
            else:
                six = i

        nums = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9}

        output = []
        for value in values.split(' '):
            output.append(str(nums.get(''.join(sorted(value)))))
        count += int(''.join(output))

    return count


if __name__ == '__main__':
    print(part1())
    print(part2())
