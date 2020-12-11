from Validator.validator import Validator
from Domain.entities import Position, Ship

class PlayerService():
    def __init__(self, player):
        self._player = player

    '''
    The function marks the squares on which the ship will be placed with an S.
    '''
    def __mark_ship_on_grid(self, bottom, top):
        if bottom.row == top.row:
            for column in range(bottom.column, top.column + 1):
                self._player.my_grid.mark_square(bottom.row, column, 'S')
        elif bottom.column == top.column:
            for row in range(bottom.row, top.row + 1):
                self._player.my_grid.mark_square(row, bottom.column, 'S')

    '''
        The function creates the top and bottom position for the ship. Validates this positions and if they are ok
        it creates a Ship object which will be added to the player's ships list. It also calls the function that marks
        on the grid the position of the ship.
    '''
    def place_ship(self, name, bottom_row, bottom_column, top_row, top_column, size):
        bottom = Position(bottom_row, bottom_column)
        top = Position(top_row, top_column)

        Validator.validate_ship_placement(bottom, top, self._player.my_grid.grid, size)

        ship = Ship(name, bottom, top, size)

        self._player.add_ship(name, ship)
        self.__mark_ship_on_grid(bottom, top)

    '''
        Function marks the square with the position: square_position, with value: value, on player's grid.
        The value can be : 0 or X.
    '''
    def mark_square_on_my_grid(self, square_position, value):
        self._player.my_grid.mark_square(square_position.row, square_position.column, value)

    '''
        Function marks the square with the position: square_position, with value: value, on player's enemy grid.
        The value can be : 0 or X.
    '''
    def mark_square_on_enemy_grid(self, square_position, value):
        self._player.enemy_grid.mark_square(square_position.row, square_position.column, value)

    '''
        The function returns the value of the square at the position: square_position, from player's grid.
    '''
    def get_value_of_square_from_my_grid(self, square_position):
        return self._player.my_grid.grid[square_position.row][square_position.column]

    '''
        The function checks if the square at the position: square_position is part of the given ship.
    '''
    def check_if_square_in_a_ship(self, ship, square_position):
        if ship.bottom.row == square_position.row and ship.bottom.column <= square_position.column <= ship.top.column:
            return True
        if ship.bottom.column == square_position.column and ship.bottom.row <= square_position.row <= ship.top.row:
            return True
        return False

    '''
        The function returns the name of the ship that was hit when the square from the: square_position was targeted.
    '''
    def get_ship_hit_name(self, square_position):
        ship_hit_name = ''
        for ship in self._player.ships:
            if self.check_if_square_in_a_ship(self._player.ships[ship], square_position):
                ship_hit_name = ship
        return ship_hit_name

    '''
        The function check's if the ship that was given as a parameter is sank or not.
    '''
    def sank_ship(self, ship):
        if self._player.ships[ship].sank():
            return True
        return False

    '''
        The function increases damage(how many of ship's squares we're hit) of the ship that has the name: ship_name.
    '''
    def increase_damage_of_ship(self, ship_name):
        self._player.ships[ship_name].damage += 1

    '''
        The function checks if the game is over. If all the player's ships have been sank then the game is over.
    '''
    def game_over(self):
        for ship in self._player.ships:
            if not self._player.ships[ship].sank():
                return False
        return True

    '''
        The function checks if the enemy grid is full with 0 or X.
    '''
    def check_if_enemy_grid_is_full(self):
        for row in self._player.my_grid.grid:
            for column in self._player.my_grid.grid[row]:
                if self._player.my_grid.grid[row][column] == '.':
                    return False
        return True

    '''
        The function returns the player's grid
    '''
    def get_my_grid(self):
        return self._player.my_grid

    '''
        The function returns the enemy player's grid.
    '''
    def get_enemy_grid(self):
        return self._player.enemy_grid
