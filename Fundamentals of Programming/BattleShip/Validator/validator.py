from Exceptions.exceptions import ValidatorException

class Validator():

    '''
    This function validates if you can place a ship in a certain place
    '''
    @staticmethod
    def validate_ship_placement(bottom, top, grid, ship_size):
        if bottom.row not in range(1, 9) or bottom.column not in range(1, 9):
            raise ValidatorException('The bottom position is not valid.')
        if top.row not in range(1, 9) or top.column not in range(1, 9):
            raise ValidatorException('The top position is not valid.')
        if bottom.row != top.row and bottom.column != top.column:
            raise ValidatorException('Impossible to place the ship here!')
        if bottom.row > top.row or bottom.column > top.column:
            raise ValidatorException('The bottom position must be smaller than the top position.')
        if bottom.row == top.row:
            if top.column - bottom.column + 1 != ship_size:
                raise ValidatorException('You must respect the ship\'s size.')
            for column in range(bottom.column, top.column + 1):
                if grid[bottom.row][column] != '.':
                    raise ValidatorException('There is already a ship there.')
        elif bottom.column == top.column:
            if top.row - bottom.row + 1 != ship_size:
                raise ValidatorException('You must respect the ship\'s size.')
            for row in range(bottom.row, top.row + 1):
                if grid[row][bottom.column] != '.':
                    raise ValidatorException('There is already a ship there.')

    '''
        This function validates if a square is part of a grid.
    '''
    @staticmethod
    def validate_square(row, column):
        if row not in range(1, 9) or column not in range(1, 9):
            raise ValidatorException('The square is not valid.')



