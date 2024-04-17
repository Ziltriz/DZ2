class BoardOutException(Exception):
    def __init__(self, x, y):
        if x or y:
            self.message = x, y
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'BoardOutException, {0}, клетка за пределами поля'.format(self.message)
        else:
            return 'BoardOutException has been raised'


class DoubleShout(Exception):
    def __init__(self, x, y):
        if x or y:
            self.message = x, y
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'DoubleShout, {0}'.format(self.message)
        else:
            return 'DoubleShout has been raised'

class IncorrectLength(Exception):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'IncorrectLength, {0}'.format(self.message)
        else:
            return 'IncorrectLength has been raised'

class BadPosition:
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'BadPosition, {0}'.format(self.message)
        else:
            return 'BadPosition has been raisede'
