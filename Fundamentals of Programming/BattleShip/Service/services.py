# from random import randrange
#
# from validator import Validator
# from Domain.entities import Position, Ship
# from errors import GameException, BattleShipException, ValidatorException
#
#
# class PlayerService():
#     def __init__(self, player):
#         self._player = player
#
#     '''
#     The function marks the squares on which the ship will be placed with an S.
#     '''
#     def __mark_ship_on_grid(self, bottom, top):
#         if bottom.row == top.row:
#             for column in range(bottom.column, top.column + 1):
#                 self._player.my_grid.mark_square(bottom.row, column, 'S')
#         elif bottom.column == top.column:
#             for row in range(bottom.row, top.row + 1):
#                 self._player.my_grid.mark_square(row, bottom.column, 'S')
#
#     '''
#         The function creates the top and bottom position for the ship. Validates this positions and if they are ok
#         it creates a Ship object which will be added to the player's ships list. It also calls the function that marks
#         on the grid the position of the ship.
#     '''
#     def place_ship(self, name, bottom_row, bottom_column, top_row, top_column, size):
#         bottom = Position(bottom_row, bottom_column)
#         top = Position(top_row, top_column)
#
#         Validator.validate_ship_placement(bottom, top, self._player.my_grid.grid, size)
#
#         ship = Ship(name, bottom, top, size)
#
#         self._player.add_ship(name, ship)
#         self.__mark_ship_on_grid(bottom, top)
#
#     '''
#         Function marks the square with the position: square_position, with value: value, on player's grid.
#         The value can be : 0 or X.
#     '''
#     def mark_square_on_my_grid(self, square_position, value):
#         self._player.my_grid.mark_square(square_position.row, square_position.column, value)
#
#     '''
#         Function marks the square with the position: square_position, with value: value, on player's enemy grid.
#         The value can be : 0 or X.
#     '''
#     def mark_square_on_enemy_grid(self, square_position, value):
#         self._player.enemy_grid.mark_square(square_position.row, square_position.column, value)
#
#     '''
#         The function returns the value of the square at the position: square_position, from player's grid.
#     '''
#     def get_value_of_square_from_my_grid(self, square_position):
#         return self._player.my_grid.grid[square_position.row][square_position.column]
#
#     '''
#         The function checks if the square at the position: square_position is part of the given ship.
#     '''
#     def check_if_square_in_a_ship(self, ship, square_position):
#         if ship.bottom.row == square_position.row and ship.bottom.column <= square_position.column <= ship.top.column:
#             return True
#         if ship.bottom.column == square_position.column and ship.bottom.row <= square_position.row <= ship.top.row:
#             return True
#         return False
#
#     '''
#         The function returns the name of the ship that was hit when the square from the: square_position was targeted.
#     '''
#     def get_ship_hit_name(self, square_position):
#         ship_hit_name = ''
#         for ship in self._player.ships:
#             if self.check_if_square_in_a_ship(self._player.ships[ship], square_position):
#                 ship_hit_name = ship
#         return ship_hit_name
#
#     '''
#         The function check's if the ship that was given as a parameter is sank or not.
#     '''
#     def sank_ship(self, ship):
#         if self._player.ships[ship].sank():
#             return True
#         return False
#
#     '''
#         The function increases damage(how many of ship's squares we're hit) of the ship that has the name: ship_name.
#     '''
#     def increase_damage_of_ship(self, ship_name):
#         self._player.ships[ship_name].damage += 1
#
#     '''
#         The function checks if the game is over. If all the player's ships have been sank then the game is over.
#     '''
#     def game_over(self):
#         for ship in self._player.ships:
#             if not self._player.ships[ship].sank():
#                 return False
#         return True
#
#     '''
#         The function checks if the enemy grid is full with 0 or X.
#     '''
#     def check_if_enemy_grid_is_full(self):
#         for row in self._player.my_grid.grid:
#             for column in self._player.my_grid.grid[row]:
#                 if self._player.my_grid.grid[row][column] == '.':
#                     return False
#         return True
#
#     '''
#         The function returns the player's grid
#     '''
#     def get_my_grid(self):
#         return self._player.my_grid
#
#     '''
#         The function returns the enemy player's grid.
#     '''
#     def get_enemy_grid(self):
#         return self._player.enemy_grid
#
#
# class ComputerService(PlayerService):
#     def __init__(self, player):
#         super().__init__(player)
#         self._squares_stack = []
#         self._mode = 'hunt'  # at first we are in hunt mode
#         self._probability_grid = self.__create_probability_grid()
#         self._available_ships = {'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2}
#
#     '''
#         The function creates the probability grid( a 8x8 matrix full with 0).
#     '''
#     def __create_probability_grid(self):
#         grid = {}
#         for row in range(1, 9):
#             grid[row] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
#         return grid
#
#     '''
#         The function generates places for computer player's ships. And then it calls the function that
#         will place the ships on the grid.
#     '''
#     def place_ships(self):
#         ships_placement = {'Battleship': 0, 'Cruiser': 0, 'Destroyer': 0}
#         ships_size = {'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2}
#         for ship in ships_placement:
#             while ships_placement[ship] == 0:
#                 try:
#                     bottom_row = randrange(1, 8 - ships_size[ship] + 1)
#                     bottom_column = randrange(1, 8)
#                     super().place_ship(ship, bottom_row, bottom_column, bottom_row + ships_size[ship] - 1, bottom_column, ships_size[ship])
#                     ships_placement[ship] = 1
#                 except BattleShipException as ex:
#                     pass
#
#     '''
#         The function increases the values from squares from start_row and start_column until finish_row and finish_column.
#         The value of the square means how probably is that some square is part of a ship.
#     '''
#     def __increase_probability(self, start_row, start_column, finish_row, finish_column):
#         for row in range(start_row, finish_row + 1):
#             for column in range(start_column, finish_column + 1):
#                 self._probability_grid[row][column] += 1
#
#     '''
#         The function checks which of the available (that are not sank) ships can fit on that row, and calls the
#         function which increases the probability of those squares.
#     '''
#     def __check_if_ships_fit_on_certain_row(self, enemy_grid, row, column):
#         for ship in self._available_ships:
#             fits = True
#             ship_size = self._available_ships[ship]
#             if column + ship_size - 1 > 8:
#                 fits = False
#             else:
#                 for pos in range(0, ship_size):
#                     if enemy_grid[row][column + pos] != '.':
#                         fits = False
#             if fits:
#                 self.__increase_probability(row, column, row, column + ship_size - 1)
#
#     '''
#         The function checks for all rows where could any of the available ships fit on that row.
#     '''
#     def __check_which_ships_fit_on_rows(self, enemy_grid):
#         for row in enemy_grid:
#             for column in range(1, 9):
#                 self.__check_if_ships_fit_on_certain_row(enemy_grid, row, column)
#
#     '''
#         The function checks which of the available (that are not sank) ships can fit on that column, and calls the
#         function which increases the probability of those squares.
#     '''
#     def __check_if_ships_fit_on_certain_column(self, enemy_grid, row, column):
#         for ship in self._available_ships:
#             ship_size = self._available_ships[ship]
#             fits = True
#             if ship_size + row - 1 > 8:
#                 fits = False
#             else:
#                 for pos in range(0, ship_size):
#                     if enemy_grid[row + pos][column] != '.':
#                         fits = False
#             if fits:
#                 self.__increase_probability(row, column, row + ship_size - 1, column)
#
#     '''
#         The function checks for all columns where could any of the available ships fit on that column.
#     '''
#     def __check_which_ships_fit_on_columns(self, enemy_grid):
#         for column in enemy_grid:
#             for row in range(1, 9):
#                 self.__check_if_ships_fit_on_certain_column(enemy_grid, row, column)
#
#     '''
#         The function completes the probability grid, taking into account the enemy_grid. Probability grid is a matrix
#         filled with numbers. Each number represents how possible is that a certain square is part of a ship.
#     '''
#     def __update_probability(self):
#         enemy_grid = super().get_enemy_grid().grid
#         self.__check_which_ships_fit_on_rows(enemy_grid)
#         self.__check_which_ships_fit_on_columns(enemy_grid)
#
#     '''
#         The function chooses a square in hunt mode. The square that has the bigger probability will be chosen.
#     '''
#     def __choose_square_hunt_mode(self):
#         higher_probability = 0
#         square_row = 0
#         square_column = 0
#         for row in range(1, 9):
#             if row % 2 == 1:
#                 columns_list = [2, 4, 6, 8]
#             else:
#                 columns_list = [1, 3, 5, 7]
#             for column in columns_list:
#                 if self._probability_grid[row][column] > higher_probability:
#                     higher_probability = self._probability_grid[row][column]
#                     square_row = row
#                     square_column = column
#         return Position(square_row, square_column)
#
#     '''
#         Hunt mode means that we choose the square that will be targeted this time
#         depending of the square's probability value.
#         Hunt mode does 3 things: -> reinitialize's the probability grid with 0's.
#                                  -> update's the probability grid with values depending on enemy grid.
#                                  -> Get's the position of the square that has the bigger probability.
#     '''
#     def __hunt_mode(self):
#         self._probability_grid = self.__create_probability_grid()
#         self.__update_probability()
#         square_position = self.__choose_square_hunt_mode()
#         return square_position
#
#     '''
#         Track mode means that in the previous round we had a HIT. So we found a ship. In squares_stack we have the
#         positions of the neighbour's squares of the square that was HIT. We take the last element from this stack and
#         consider it as the present targeted square. If the squares from the stack are no longer available for targeting
#         we return a position 0,0.
#     '''
#     def __track_mode(self):
#         while len(self._squares_stack) != 0:
#             if super().get_enemy_grid().grid[self._squares_stack[-1].row][self._squares_stack[-1].column] == '.':
#                 return self._squares_stack[-1]
#             else:
#                 self._squares_stack.pop()
#         return Position(0, 0)
#
#     '''
#         The function returns the position of the targeted square depending on the mode that computer plays now (hunt or
#         track).
#     '''
#     def choose_square(self):
#         if self._mode == 'hunt':
#             square_position = self.__hunt_mode()
#         elif self._mode == 'track':
#             square_position = self.__track_mode()
#             if square_position.row == 0 or square_position.column == 0:
#                 square_position = self.__hunt_mode()
#                 self._mode = 'hunt'
#         return square_position
#
#     '''
#         The function returns the name of the ship that was sunk. The name of the ship is part of the message.
#     '''
#     def __get_ship_name_from_message(self, message):
#         if message.find('Battleship') != -1:
#             return 'Battleship'
#         if message.find('Cruiser') != -1:
#             return 'Cruiser'
#         if message.find('Destroyer') != -1:
#             return 'Destroyer'
#
#     '''
#         The function does the following:
#         If the message is HIT: it adds to squares_stack the positions of the neighbours of the square that was hit, and
#                                 sets the mode to: track.
#         If the message is MISS: if the square_stack is empty the mode is changed to: hunt;
#                                 else we pop the last element from the square_stack;
#         If the message contains the word: sank it means that a ship was sank, so we remove that ship from the available
#         ships and we enter in hunt mode again.
#     '''
#     def changes_after_a_move(self, message, square_position):
#         if message == 'HIT':
#             # left
#             if square_position.column - 1 > 0:
#                 self._squares_stack.append(Position(square_position.row, square_position.column - 1))
#             # down
#             if square_position.row + 1 < 9:
#                 self._squares_stack.append(Position(square_position.row + 1, square_position.column))
#             # right
#             if square_position.column + 1 < 9:
#                 self._squares_stack.append(Position(square_position.row, square_position.column + 1))
#             # up
#             if square_position.row - 1 > 0:
#                 self._squares_stack.append(Position(square_position.row - 1, square_position.column))
#             self._mode = 'track'
#         elif message == 'MISS':
#             if len(self._squares_stack) == 0:
#                 self._mode = 'hunt'
#             else:
#                 self._mode = 'track'
#                 self._squares_stack.pop()
#         elif message.find('sank'):
#             message = self.__get_ship_name_from_message(message)
#             if len(self._squares_stack) == 0:
#                 self._mode = 'hunt'
#             self._available_ships.pop(message)
#
# class GameService:
#     def __init__(self, human_player_service, computer_player_service):
#         self.__human_player_service = human_player_service
#         self.__computer_player_service = computer_player_service
#
#     '''
#         The function determines in which direction( right / down or both) a human's ship can be placed.
#     '''
#     def get_ship_possible_placing_for_human(self, bottom_position_list, ship_size):
#         square_bottom_position = Position(bottom_position_list[0], bottom_position_list[1])
#         grid = self.__human_player_service.get_my_grid().grid
#
#         ship_possible_position = {}
#
#         right_square = Position(square_bottom_position.row, square_bottom_position.column + ship_size - 1)
#         down_square = Position(square_bottom_position.row + ship_size - 1, square_bottom_position.column)
#
#         try:
#             Validator.validate_ship_placement(square_bottom_position, right_square, grid, ship_size)
#             ship_possible_position['right'] = right_square
#         except ValidatorException:
#             pass
#
#         try:
#             Validator.validate_ship_placement(square_bottom_position, down_square, grid, ship_size)
#             ship_possible_position['down'] = down_square
#         except ValidatorException:
#             pass
#
#         return ship_possible_position
#
#     '''
#         Function that calls another function which adds a ship to the human player.
#     '''
#     def human_player_add_ship(self, name, bottom_row, bottom_column, top_row, top_column, size):
#         self.__human_player_service.place_ship(name, bottom_row, bottom_column, top_row, top_column, size)
#
#     '''
#         Function that calls the function that places the ship for the computer player.
#     '''
#     def place_computer_ships(self):
#         self.__computer_player_service.place_ships()
#
#     '''
#         This function returns the message:
#             notover: if the game is not done yet;
#             name of the player who won + won: if a certain player won;
#             draw: if the game ended with a draw;
#     '''
#     def __check_if_game_over(self, other_player_service, active_player, active_player_service):
#         if other_player_service.game_over():
#             return active_player + ' won!'
#         if other_player_service.check_if_enemy_grid_is_full() and active_player_service.check_if_enemy_grid_is_full():
#             return 'Game ended with a draw!'
#         return 'notover'
#
#     '''
#         This function makes the hit on the targeted square(that has the position square_position) and returns the
#         appropriate message: ship_hit_name + sank if a ship was sank,
#                              HIT if the square is part of a ship,
#                              MISS otherwise.
#     '''
#     def __game_move(self, active_player_service, other_player_service, square_position):
#         square_value = other_player_service.get_value_of_square_from_my_grid(square_position)
#         if square_value == '0' or square_value == 'X':
#             raise GameException('You already hit that square.')
#         elif square_value == '.':
#             other_player_service.mark_square_on_my_grid(square_position, '0')
#             active_player_service.mark_square_on_enemy_grid(square_position, '0')
#             return 'MISS'
#         elif square_value == 'S':
#             ship_hit_name = other_player_service.get_ship_hit_name(square_position)
#             other_player_service.increase_damage_of_ship(ship_hit_name)
#             active_player_service.mark_square_on_enemy_grid(square_position, 'X')
#             other_player_service.mark_square_on_my_grid(square_position, 'X')
#             if other_player_service.sank_ship(ship_hit_name):
#                 return ship_hit_name + ' sank!'
#             return 'HIT'
#
#     '''
#         This function returns the player's grid.
#     '''
#     def get_player_grid(self, player):
#         if player == 'human':
#             return self.__human_player_service.get_my_grid()
#         elif player == 'computer':
#             return self.__computer_player_service.get_my_grid()
#
#     '''
#         This function returns the enemy player's grid.
#     '''
#     def get_enemy_grid(self, player):
#         if player == 'human':
#             return self.__human_player_service.get_enemy_grid()
#         elif player == 'computer':
#             return self.__computer_player_service.get_enemy_grid()
#
#     '''
#         This function plays computer's turn.
#     '''
#     def computer_turn(self):
#         square_position = self.__computer_player_service.choose_square()
#
#         returned_value = self.__game_move(self.__computer_player_service, self.__human_player_service, square_position)
#         message = self.__check_if_game_over(self.__human_player_service, 'computer', self.__computer_player_service)
#
#         self.__computer_player_service.changes_after_a_move(returned_value, square_position)
#
#         if message == 'notover':
#             return returned_value
#         else:
#             return message
#
#     '''
#         This function plays human's turn.
#     '''
#     def human_turn(self, square_row, square_column):
#         square_position = Position(square_row, square_column)
#         Validator.validate_square(square_position.row, square_position.column)
#
#         returned_value = self.__game_move(self.__human_player_service, self.__computer_player_service, square_position)
#         message = self.__check_if_game_over(self.__computer_player_service, 'human', self.__human_player_service)
#
#         if message == 'notover':
#             return returned_value
#         else:
#             return message
#
#
#
