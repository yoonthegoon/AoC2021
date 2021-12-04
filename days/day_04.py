# https://adventofcode.com/2021/day/4

import requests

cookie = open('.config', 'r').read()
r = requests.get('https://adventofcode.com/2021/day/4/input', cookies=dict(session=cookie))

bingo = r.text.split('\n\n')[:-1]

instructions = [int(i) for i in bingo[0].split(',')]
boards = bingo[1:]


class BingoBoard:
    def __init__(self, string):
        board, called = dict(), dict()

        for i, num in enumerate('12345'):
            for j, let in enumerate('abcde'):
                board[f'{let}{num}'] = int(string.split('\n')[i][3*j:3*j+2])
                called[f'{let}{num}'] = None

        self.board, self.called = board, called
        self.board_sum = 0
        self.win, self.won = False, False

    def draw(self, number):
        if number in self.board.values():
            for key, value in self.board.items():
                if value == number:
                    self.board[key] = None
                    self.called[key] = value

        rows = [[self.called[f'{let}{num}'] for let in 'abcde'] for num in '12345']
        cols = [[self.called[f'{let}{num}'] for num in '12345'] for let in 'abcde']
        for row in rows:
            if len(list(filter(lambda x: type(x) is int, row))) == 5:
                self.win = True
        for col in cols:
            if len(list(filter(lambda x: type(x) is int, col))) == 5:
                self.win = True

    def sums(self):
        if self.won:
            return 0

        for value in self.board.values():
            if type(value) is int:
                self.board_sum += value

        self.won = True

        return self.board_sum


def part1():
    bingo_boards = [BingoBoard(board) for board in boards]
    for instruction in instructions:
        for bingo_board in bingo_boards:
            bingo_board.draw(instruction)
            if bingo_board.win:
                return bingo_board.sums() * instruction


def part2():
    winning_boards = []

    bingo_boards = [BingoBoard(board) for board in boards]
    for instruction in instructions:
        for bingo_board in bingo_boards:
            bingo_board.draw(instruction)
            if bingo_board.win:
                winning_boards.append(bingo_board.sums() * instruction)

    return list(filter(lambda i: i != 0, winning_boards))[-1]


if __name__ == '__main__':
    print(part1())
    print(part2())
