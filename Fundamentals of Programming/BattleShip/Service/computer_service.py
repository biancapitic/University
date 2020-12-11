from random import randrange

from Domain.entities import Position
from Exceptions.exceptions import BattleShipException
from Service.player_service import PlayerService


class ComputerService(PlayerService):
    def __init__(self, player):
        super().__init__(player)
        self._squares_stack = []
        self._mode = 'hunt'  # at first we are in hunt mode
        self._probability_grid = self.__create_probability_grid()
        self._available_ships = {'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2}

    '''
        The function creates the probability grid( a 8x8 matrix full with 0).
    '''
    def __create_probability_grid(self):
        grid = {}
        for row in range(1, 9):
            grid[row] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        return grid

    '''
        The function generates places for computer player's ships. And then it calls the function that 
        will place the ships on the grid.
    '''
    def place_ships(self):
        ships_placement = {'Battleship': 0, 'Cruiser': 0, 'Destroyer': 0}
        ships_size = {'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2}
        for ship in ships_placement:
            while ships_placement[ship] == 0:
                try:
                    bottom_row = randrange(1, 8 - ships_size[ship] + 1)
                    bottom_column = randrange(1, 8)
                    super().place_ship(ship, bottom_row, bottom_column, bottom_row + ships_size[ship] - 1, bottom_column, ships_size[ship])
                    ships_placement[ship] = 1
                except BattleShipException as ex:
                    pass

    '''
        The function increases the values from squares from start_row and start_column until finish_row and finish_column.
        The value of the square means how probably is that some square is part of a ship.
    '''
    def __increase_probability(self, start_row, start_column, finish_row, finish_column):
        for row in range(start_row, finish_row + 1):
            for column in range(start_column, finish_column + 1):
                self._probability_grid[row][column] += 1

    '''
        The function checks which of the available (that are not sank) ships can fit on that row, and calls the
        function which increases the probability of those squares.
    '''
    def __check_if_ships_fit_on_certain_row(self, enemy_grid, row, column):
        for ship in self._available_ships:
            fits = True
            ship_size = self._available_ships[ship]
            if column + ship_size - 1 > 8:
                fits = False
            else:
                for pos in range(0, ship_size):
                    if enemy_grid[row][column + pos] != '.':
                        fits = False
            if fits:
                self.__increase_probability(row, column, row, column + ship_size - 1)

    '''
        The function checks for all rows where could any of the available ships fit on that row.
    '''
    def __check_which_ships_fit_on_rows(self, enemy_grid):
        for row in enemy_grid:
            for column in range(1, 9):
                self.__check_if_ships_fit_on_certain_row(enemy_grid, row, column)

    '''
        The function checks which of the available (that are not sank) ships can fit on that column, and calls the
        function which increases the probability of those squares.
    '''
    def __check_if_ships_fit_on_certain_column(self, enemy_grid, row, column):
        for ship in self._available_ships:
            ship_size = self._available_ships[ship]
            fits = True
            if ship_size + row - 1 > 8:
                fits = False
            else:
                for pos in range(0, ship_size):
                    if enemy_grid[row + pos][column] != '.':
                        fits = False
            if fits:
                self.__increase_probability(row, column, row + ship_size - 1, column)

    '''
        The function checks for all columns where could any of the available ships fit on that column.
    '''
    def __check_which_ships_fit_on_columns(self, enemy_grid):
        for column in enemy_grid:
            for row in range(1, 9):
                self.__check_if_ships_fit_on_certain_column(enemy_grid, row, column)

    '''
        The function completes the probability grid, taking into account the enemy_grid. Probability grid is a matrix
        filled with numbers. Each number represents how possible is that a certain square is part of a ship. 
    '''
    def __update_probability(self):
        enemy_grid = super().get_enemy_grid().grid
        self.__check_which_ships_fit_on_rows(enemy_grid)
        self.__check_which_ships_fit_on_columns(enemy_grid)

    '''
        The function chooses a square in hunt mode. The square that has the bigger probability will be chosen.
    '''
    def __choose_square_hunt_mode(self):
        higher_probability = 0
        square_row = 0
        square_column = 0
        for row in range(1, 9):
            if row % 2 == 1:
                columns_list = [2, 4, 6, 8]
            else:
                columns_list = [1, 3, 5, 7]
            for column in columns_list:
                if self._probability_grid[row][column] > higher_probability:
                    higher_probability = self._probability_grid[row][column]
                    square_row = row
                    square_column = column
        return Position(square_row, square_column)

    '''
        Hunt mode means that we choose the square that will be targeted this time
        depending of the square's probability value. 
        Hunt mode does 3 things: -> reinitialize's the probability grid with 0's.
                                 -> update's the probability grid with values depending on enemy grid.
                                 -> Get's the position of the square that has the bigger probability.
    '''
    def __hunt_mode(self):
        self._probability_grid = self.__create_probability_grid()
        self.__update_probability()
        square_position = self.__choose_square_hunt_mode()
        return square_position

    '''
        Track mode means that in the previous round we had a HIT. So we found a ship. In squares_stack we have the
        positions of the neighbour's squares of the square that was HIT. We take the last element from this stack and
        consider it as the present targeted square. If the squares from the stack are no longer available for targeting
        we return a position 0,0.
    '''
    def __track_mode(self):
        while len(self._squares_stack) != 0:
            if super().get_enemy_grid().grid[self._squares_stack[-1].row][self._squares_stack[-1].column] == '.':
                return self._squares_stack[-1]
            else:
                self._squares_stack.pop()
        return Position(0, 0)

    '''
        The function returns the position of the targeted square depending on the mode that computer plays now (hunt or
        track).
    '''
    def choose_square(self):
        if self._mode == 'hunt':
            square_position = self.__hunt_mode()
        elif self._mode == 'track':
            square_position = self.__track_mode()
            if square_position.row == 0 or square_position.column == 0:
                square_position = self.__hunt_mode()
                self._mode = 'hunt'
        return square_position

    '''
        The function returns the name of the ship that was sunk. The name of the ship is part of the message.
    '''
    def __get_ship_name_from_message(self, message):
        if message.find('Battleship') != -1:
            return 'Battleship'
        if message.find('Cruiser') != -1:
            return 'Cruiser'
        if message.find('Destroyer') != -1:
            return 'Destroyer'

    '''
        The function does the following:
        If the message is HIT: it adds to squares_stack the positions of the neighbours of the square that was hit, and
                                sets the mode to: track.
        If the message is MISS: if the square_stack is empty the mode is changed to: hunt;
                                else we pop the last element from the square_stack;
        If the message contains the word: sank it means that a ship was sank, so we remove that ship from the available 
        ships and we enter in hunt mode again.     
    '''
    def changes_after_a_move(self, message, square_position):
        if message == 'HIT':
            # left
            if square_position.column - 1 > 0:
                self._squares_stack.append(Position(square_position.row, square_position.column - 1))
            # down
            if square_position.row + 1 < 9:
                self._squares_stack.append(Position(square_position.row + 1, square_position.column))
            # right
            if square_position.column + 1 < 9:
                self._squares_stack.append(Position(square_position.row, square_position.column + 1))
            # up
            if square_position.row - 1 > 0:
                self._squares_stack.append(Position(square_position.row - 1, square_position.column))
            self._mode = 'track'
        elif message == 'MISS':
            if len(self._squares_stack) == 0:
                self._mode = 'hunt'
            else:
                self._mode = 'track'
                self._squares_stack.pop()
        elif message.find('sank'):
            message = self.__get_ship_name_from_message(message)
            if len(self._squares_stack) == 0:
                self._mode = 'hunt'
            self._available_ships.pop(message)