class Ship():
    def __init__(self, name, bottom, top, size):
        self.__name = name
        self.__bottom = bottom  # line, column
        self.__top = top  # line, column
        self.__size = size
        self.__damage = 0

    @property
    def name(self):
        return self.__name

    @property
    def bottom(self):
        return self.__bottom

    @property
    def top(self):
        return self.__top

    @property
    def size(self):
        return self.__size

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, new_value):
        self.__damage = new_value

    def sank(self):
        if self.__damage == self.__size:
            return True
        return False


class Grid:
    def __init__(self):
        self.__grid = self.__create_grid()

    def __create_grid(self):
        grid = {}
        for line in range(1, 9):
            grid[line] = {1: '.', 2: '.', 3: '.', 4: '.', 5: '.', 6: '.', 7: '.', 8: '.'}
        return grid

    @property
    def grid(self):
        return self.__grid

    def mark_square(self, row, column, value):
        self.__grid[row][column] = value

    def print_grid(self):
        print('    ', 'A', '|', 'B', '|', 'C', '|', 'D', '|', 'E', '|', 'F', '|', 'G', '|', 'H', '|')
        for row in range(1, 9):
            print(row, ' |', end='')
            for column in self.grid[row]:
                print('', self.grid[row][column], '|', end='')
            print()


class Player():
    def __init__(self, my_grid, enemy_grid):
        self.__my_grid = my_grid
        self.__enemy_grid = enemy_grid
        self.__ships = {}

    @property
    def my_grid(self):
        return self.__my_grid

    @property
    def enemy_grid(self):
        return self.__enemy_grid

    @property
    def ships(self):
        return self.__ships

    def add_ship(self, name, ship):
        self.__ships[name] = ship


class Position():
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column
