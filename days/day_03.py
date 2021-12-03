# https://adventofcode.com/2021/day/3

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/3/input', cookies=dict(session=cookie))

report = r.text.split('\n')[:-1]


def part1():
    gamma, epsilon = '', ''

    bits = dict()
    for i in 'abcdefghijkl':
        bits[i] = []

    for i in report:
        for j, k in enumerate(i):
            bits['abcdefghijkl'[j]].append(float(k))

    for key in bits.keys():
        bits[key] = sum(bits[key]) / len(bits[key])
        bits[key] = int(bits[key] + .5)

        gamma += str(bits[key])
        epsilon += '0' if bits[key] else '1'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def part2():
    report = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010'
    ]

    o2, co2 = '', ''

    o2_report, co2_report = report, report

    for i in range(5):
        if len(o2_report) == 1:
            break

        common = '1' if sum(float(j[i]) for j in o2_report) / len(o2_report) + .5 >= 0.5 else '0'
        temp_o2 = o2_report
        for j in temp_o2:
            if j[i] != common:
                o2_report.remove(j)
            print(o2_report)
        o2 += common

    # for i in range(5):
    #     uncommon = '0' if sum(float(j[i]) for j in co2_report) / len(co2_report) >= 0.5 else '1'
    #     for j in co2_report:
    #         if j[i] != uncommon:
    #             co2_report.remove(j)
    #
    #     co2 += uncommon
    print(o2, co2)
    # o2 = int(o2, 2)
    # co2 = int(co2, 2)
    #
    # return o2 * co2


if __name__ == '__main__':
    print(part1())
    print(part2())
