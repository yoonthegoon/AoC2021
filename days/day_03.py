# https://adventofcode.com/2021/day/3

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/3/input', cookies=dict(session=cookie))

report = r.text.split('\n')[:-1]


def part1():
    gamma = ''.join(list(map(lambda i: str(int(sum([float(bits[i]) for bits in report]) / len(report) + 0.5)),
                             range(len(report[0])))))
    epsilon = ''.join('0' if int(i) else '1' for i in gamma)

    gamma, epsilon = int(gamma, 2), int(epsilon, 2)

    return gamma * epsilon


def part2():
    o2_report, co2_report = report, report

    for i in range(len(o2_report[0])):
        if len(o2_report) == 1:
            break

        o2_report = list(filter(lambda j: j[i] == str(int(sum(map(
            lambda k: float(k[i]), o2_report)) / len(o2_report) + 0.5)), o2_report))

    for i in range(len(co2_report)):
        if len(co2_report) == 1:
            break

        co2_report = list(filter(lambda j: j[i] != str(int(sum(map(
            lambda k: float(k[i]), co2_report)) / len(co2_report) + 0.5)), co2_report))

    o2, co2 = int(o2_report[0], 2), int(co2_report[0], 2)

    return o2 * co2


if __name__ == '__main__':
    print(part1())
    print(part2())
