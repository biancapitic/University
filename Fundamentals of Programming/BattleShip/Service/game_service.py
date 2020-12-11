from Validator.validator import Validator
from Domain.entities import Position
from Exceptions.exceptions import GameException, ValidatorException

class GameService:
    def __init__(self, human_player_service, computer_player_service):
        self.__human_player_service = human_player_service
        self.__computer_player_service = computer_player_service

    '''
        The function determines in which direction( right / down or both) a human's ship can be placed.
    '''
    def get_ship_possible_placing_for_human(self, bottom_position_list, ship_size):
        square_bottom_position = Position(bottom_position_list[0], bottom_position_list[1])
        grid = self.__human_player_service.get_my_grid().grid

        ship_possible_position = {}

        right_square = Position(square_bottom_position.row, square_bottom_position.column + ship_size - 1)
        down_square = Position(square_bottom_position.row + ship_size - 1, square_bottom_position.column)

        try:
            Validator.validate_ship_placement(square_bottom_position, right_square, grid, ship_size)
            ship_possible_position['right'] = right_square
        except ValidatorException:
            pass

        try:
            Validator.validate_ship_placement(square_bottom_position, down_square, grid, ship_size)
            ship_possible_position['down'] = down_square
        except ValidatorException:
            pass

        return ship_possible_position

    '''
        Function that calls another function which adds a ship to the human player.
    '''
    def human_player_add_ship(self, name, bottom_row, bottom_column, top_row, top_column, size):
        self.__human_player_service.place_ship(name, bottom_row, bottom_column, top_row, top_column, size)

    '''
        Function that calls the function that places the ship for the computer player.
    '''
    def place_computer_ships(self):
        self.__computer_player_service.place_ships()

    '''
        This function returns the message:
            notover: if the game is not done yet;
            name of the player who won + won: if a certain player won;
            draw: if the game ended with a draw;
    '''
    def __check_if_game_over(self, other_player_service, active_player, active_player_service):
        if other_player_service.game_over():
            return active_player + ' won!'
        if other_player_service.check_if_enemy_grid_is_full() and active_player_service.check_if_enemy_grid_is_full():
            return 'Game ended with a draw!'
        return 'notover'

    '''
        This function makes the hit on the targeted square(that has the position square_position) and returns the
        appropriate message: ship_hit_name + sank if a ship was sank, 
                             HIT if the square is part of a ship, 
                             MISS otherwise.
    '''
    def __game_move(self, active_player_service, other_player_service, square_position):
        square_value = other_player_service.get_value_of_square_from_my_grid(square_position)
        if square_value == '0' or square_value == 'X':
            raise GameException('You already hit that square.')
        elif square_value == '.':
            other_player_service.mark_square_on_my_grid(square_position, '0')
            active_player_service.mark_square_on_enemy_grid(square_position, '0')
            return 'MISS'
        elif square_value == 'S':
            ship_hit_name = other_player_service.get_ship_hit_name(square_position)
            other_player_service.increase_damage_of_ship(ship_hit_name)
            active_player_service.mark_square_on_enemy_grid(square_position, 'X')
            other_player_service.mark_square_on_my_grid(square_position, 'X')
            if other_player_service.sank_ship(ship_hit_name):
                return ship_hit_name + ' sank!'
            return 'HIT'

    '''
        This function returns the player's grid.
    '''
    def get_player_grid(self, player):
        if player == 'human':
            return self.__human_player_service.get_my_grid()
        elif player == 'computer':
            return self.__computer_player_service.get_my_grid()

    '''
        This function returns the enemy player's grid.
    '''
    def get_enemy_grid(self, player):
        if player == 'human':
            return self.__human_player_service.get_enemy_grid()
        elif player == 'computer':
            return self.__computer_player_service.get_enemy_grid()

    '''
        This function plays computer's turn.
    '''
    def computer_turn(self):
        square_position = self.__computer_player_service.choose_square()

        returned_value = self.__game_move(self.__computer_player_service, self.__human_player_service, square_position)
        message = self.__check_if_game_over(self.__human_player_service, 'computer', self.__computer_player_service)

        self.__computer_player_service.changes_after_a_move(returned_value, square_position)

        if message == 'notover':
            return returned_value
        else:
            return message

    '''
        This function plays human's turn.
    '''
    def human_turn(self, square_row, square_column):
        square_position = Position(square_row, square_column)
        Validator.validate_square(square_position.row, square_position.column)

        returned_value = self.__game_move(self.__human_player_service, self.__computer_player_service, square_position)
        message = self.__check_if_game_over(self.__computer_player_service, 'human', self.__human_player_service)

        if message == 'notover':
            return returned_value
        else:
            return message
