import random

from errors import *


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'*'


class Ship:
    def __init__(self, length, start_point, orientation, health):
        self.length = int(length)
        self.start_point = start_point
        self.orientation = orientation
        self.health = health

    def dots(self):
        sp = self.start_point
        all_dots = []
        if self.orientation == 'v':
            for i in range(self.length):
                dot = [sp[0], sp[1]]
                all_dots.append(dot)
                sp[0] += 1

        if self.orientation == 'h':
            for i in range(self.length):
                dot = [sp[0], sp[1]]
                all_dots.append(dot)
                sp[1] += 1
        self.start_point = all_dots[0]
        return all_dots


class Board:

    def __init__(self, all_ships, hid, ship_alive):
        self.all_ships = list(all_ships)
        self.hid = bool(hid)
        self.ship_alive = ship_alive
        board = [['0'] * 6 for a in range(6)]
        x = 1
        for i in range(6):
            board[i].insert(0, str(x))
            x += 1
        self.board = board

    def add_ship(self, ship):
        ship_dots = ship.dots()
        err = 0
        err1 = 0
        for u in range(len(ship_dots)):
            if (0 < ship_dots[u][0] >= 5) or (1 <= ship_dots[u][1] >= 6):
                err = 1
                return err

        if err == 0:
            eq1 = []
            dots = []
            if len(self.all_ships) == 0:
                pass
            else:
                for a in range(len(self.all_ships)):
                    eq1.append(self.contour(self.all_ships[a], self.all_ships[a].dots()))
                    dots.append(self.all_ships[a].dots())

            for c in ship_dots:
                for i in range(len(eq1)):
                    for j in eq1[i]:
                        if c == j or c == dots[i]:
                            err1 = 1
                            return err1

            if err1 == 0:
                self.all_ships.append(ship)

            if len(self.all_ships) == 6:
                self.ship_alive = 10
                return err1

    def contour(self, ship, ship_dots):
        eq = []
        eq1 = []
        for a in range(7):
            for j in range(7):
                for i in range(len(ship_dots)):
                    if ship.length == 1:
                        if (a + 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                a - 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                a == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                a == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                a + 1 == ship_dots[i][0] and j == ship_dots[i][1]) or (
                                a - 1 == ship_dots[i][0] and j == ship_dots[i][1]) or (
                                a + 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                a - 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]):
                            eq.append([a, j])
                    if ship.orientation == 'v':
                        if ship.length == 2:
                            if (a == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j == ship_dots[i][1] and a - 1 != ship_dots[0][0]) or (
                                    a + 1 == ship_dots[i][0] and j == ship_dots[i][1] and a + 1 != ship_dots[1][0]):
                                eq.append([a, j])
                        if ship.length == 3:
                            if (a == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 2 == ship_dots[1][0] and j == ship_dots[i][1]) or (
                                    a + 2 == ship_dots[1][0] and j == ship_dots[i][1]):
                                eq.append([a, j])
                    if ship.orientation == 'h':
                        if ship.length == 2:
                            if (a == ship_dots[i][0] and j + 1 == ship_dots[i][1] and j != ship_dots[0][1]) or (
                                    a == ship_dots[i][0] and j - 1 == ship_dots[i][1] and j != ship_dots[1][1]) or (
                                    a + 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j == ship_dots[i][1]):
                                eq.append([a, j])
                        if ship.length == 3:
                            if (a == ship_dots[1][0] and j + 2 == ship_dots[1][1]) or (
                                    a == ship_dots[1][0] and j - 2 == ship_dots[1][1]) or (
                                    a + 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a + 1 == ship_dots[i][0] and j - 1 == ship_dots[i][1]) or (
                                    a - 1 == ship_dots[i][0] and j + 1 == ship_dots[i][1]):
                                eq.append([a, j])

        for i in range(len(eq)):
            if 0 <= eq[i][0] < 6 and 0 < eq[i][1] <= 6:
                eq1.append(eq[i])

        try:
            for b in range(len(eq1)):
                sh = [eq1[b][0], eq1[b][1]]
                self.out(sh)

        except BadPosition as e:
            print(e)
            return
        return eq1

    def print_hid(self, board, hid):
        if hid:

            print('     Доска компьютера      ')
            print('    1 | 2 | 3 | 4 | 5 | 6 ')
            print('\n'.join(map(' | '.join, board)))
        else:
            ship_dots = []
            for i in range(len(self.all_ships)):
                ship_dots.append(self.all_ships[i].dots())
            for a in range(len(ship_dots)):
                for c in range(len(ship_dots[a])):
                    self.board[ship_dots[a][c][0]][ship_dots[a][c][1]] = 'K'
                    eq1 = self.contour(self.all_ships[a], ship_dots[c])
                    for c in range(len(eq1)):
                        if self.board[eq1[c][0]][eq1[c][1]] == 'T' or self.board[eq1[c][0]][eq1[c][1]] == 'K':
                            c += 1
                        else:
                            self.board[eq1[c][0]][eq1[c][1]] = 'T'
            print('     Твоя доска      ')
            print('    1 | 2 | 3 | 4 | 5 | 6 ')
            print('\n'.join(map(' | '.join, board)))

    def out(self, shot):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if shot[0] < len(self.board[i]) or shot[1] < len(self.board[i][j]) or shot[0] > len(
                        self.board[i]) or shot[1] > len(self.board[i][j]):
                    return False
                else:
                    return True

    def shot(self, shot):
        ship_dots = []
        sh = 0
        for i in range(len(self.all_ships)):
            ship_dots.append(self.all_ships[i].dots())
        print(ship_dots)
        try:
            if not self.out(shot):
                for a in range(len(ship_dots)):
                    for j in range(len(ship_dots[a])):
                        if shot == ship_dots[a][j]:
                            sh = 1
                            self.all_ships[a].health = self.all_ships[a].health - 1
                            if self.all_ships[a].health == 0:
                                print('Убит!')
                            self.board[shot[0]][shot[1]] = 'X'
                            self.print_hid(self.board, self.hid)
                            self.ship_alive = self.ship_alive - 1
                            print('Попадание!')
                            return sh

                if sh == 0:
                    self.board[shot[0]][shot[1]] = 'T'
                    self.print_hid(self.board, self.hid)
                    print('Промах!')
                    return sh

        except DoubleShout as e:
            print(e)
        else:
            self.print_hid(self.board, self.hid)
            return sh


class Player:
    def __init__(self, my_board, enemy_board):
        self.my_board: Board = my_board
        self.enemy_board: Board = enemy_board

    def ask(self):
        return

    def move(self):
        while True:
            shot = self.ask()
            if self.enemy_board.shot(shot) == 0:
                break


class User(Player):

    def ask(self):
        shot = input('Куда делаем выстрел? (x, y) ')
        parse = shot.strip('[]').replace(' ', '').split(',')
        shot = [int(i) for i in parse]
        shot[0] = shot[0] - 1
        return shot


class Ai(Player):

    def ask(self):
        shot = [random.randint(0, 5), random.randint(1, 6)]

        return shot


class Game:
    def __init__(self):
        self.user = User
        self.board_user = Board
        self.ai = Ai
        self.board_ai = Board

    def random_board(self):
        len_arr = [3, 2, 2, 1, 1, 1]
        i = 0
        a = 0
        l = 0
        all_ships = []
        orient = ['v', 'h']
        hid = False
        ship_alive = len(all_ships)
        board = Board(all_ships, hid, ship_alive)
        while True:
            length = len_arr[i]
            sp = [random.randint(0, 5), random.randint(1, 6)]
            orientation = random.choice(orient)
            health = length
            ship = Ship(length, sp, orientation, health)
            if board.add_ship(ship) == 1:
                board.all_ships.clear()
            i = len(board.all_ships)
            a += 1
            if len(board.all_ships) == 6 and l == 0:
                self.board_user = board
                board.hid = False
                all_ships = []
                board = Board(all_ships, board.hid, ship_alive)
                i = 0
                a = 0
                l = 1
            if len(board.all_ships) == 6 and l == 1:
                board.hid = True
                self.board_ai = board
                i = 0
                a = 0
                l = 2
            if l == 2:
                return self.board_user, self.board_ai

            if a > 2000:
                board.all_ships = []
                i = 0
                board = Board(all_ships, hid, ship_alive)
                a = 0

    def greet(self):
        print('Здравствуй игрок!')
        print('Играем в морской бой!')
        print('Вводи номера точек через запятую и потопи все корабли противника')
        self.random_board()

    def loop(self):
        user = self.user(self.board_user, self.board_ai)
        ai = self.ai(self.board_ai, self.board_user)
        user.my_board.print_hid(user.my_board.board, user.my_board.hid)
        ai.my_board.print_hid(ai.my_board.board, ai.my_board.hid)
        while True:
            user.move()
            print('Ход компьютера')
            ai.move()
            if user.my_board.ship_alive == 0:
                print('Вы проиграли! Удачи в следующий раз')
                exit()
            if ai.my_board.ship_alive == 0:
                print('Вы победили! Поздравляем!')
                exit()

    def start(self):
        Game.greet(self)
        Game.loop(self)


# pl_ship = Ship(3, [1, 1], 'vertical', 3)
# pl_ship.dots()
# player = Player()
b1 = Board([], True, 4)
b2 = Game()
Game.start(b2)
