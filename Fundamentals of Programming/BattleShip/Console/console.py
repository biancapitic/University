from Exceptions.exceptions import BattleShipException


class UI():
    def __init__(self, game_service):
        self.__game_service = game_service

    def __print_game_rules(self):
        print('GAME RULES: ')
        print('. -> a square that hasn\'t been chosen yet\n'
              '0 -> a square that was chosen and it resulted a MISS;\n'
              'X -> a square that was chosen and it resulted a HIT;\n'
              'S -> a square which is part of a ship;\n'
              'The bottom position of a ship must be smaller than it\'s top position.')

    def print_grids(self, player, first_grid):
        player_grid = self.__game_service.get_player_grid(player)
        enemy_grid = self.__game_service.get_enemy_grid(player)

        if first_grid == 'mygrid':
            print("MY GRID")
            player_grid.print_grid()
            print("ENEMY GRID")
            enemy_grid.print_grid()
        else:
            print("ENEMY GRID")
            enemy_grid.print_grid()
            print("MY GRID")
            player_grid.print_grid()

    def __read_square_position(self):
        columns = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        row = int(input('Enter row of square: '))
        if row not in [1, 2, 3, 4, 5, 6, 7, 8]:
            raise BattleShipException('The row is invalid!')
        column = input('Enter column of square: ')
        if column not in columns:
            raise BattleShipException('The column is invalid!')
        column = columns[column]
        return row, column

    def __read_ship_place(self, ship_size):
        try:
            print('Enter coordinates for the ship\'s bottom:')
            bottom_position = self.__read_square_position()
            possible_positions = self.__game_service.get_ship_possible_placing_for_human(bottom_position, ship_size)
            if len(possible_positions) == 0:
                raise BattleShipException("You can't place the ship there. \n"
                                          "The bottom position must be smaller than the top position. Try again.\n")
            while True:
                print('Choose the direction where you want to place the ship. Directions:')
                for position in possible_positions:
                    print(position)
                direction = input("Enter one direction from the one\'s listed above: ")
                if direction not in possible_positions:
                    print("The direction was wrong, choose something else from the list.")
                else:
                    break
            top_position = possible_positions[direction]
            return bottom_position[0], bottom_position[1], top_position.row, top_position.column
        except ValueError:
            return 'Row and column must be integers.'

    def __place_human_ships(self):
        ships_size = {'Battleship': 4, 'Cruiser': 3, 'Destroyer': 2}
        ships_placement = {'Battleship': 0, 'Cruiser': 0, 'Destroyer': 0}
        self.print_grids('human', 'enemygrid')
        for ship in ships_placement:
            while ships_placement[ship] == 0:
                try:
                    print("Enter coordinates for " + ship + " that has length " + str(ships_size[ship]) + ":")
                    positions = self.__read_ship_place(ships_size[ship])
                    self.__game_service.human_player_add_ship(ship, positions[0], positions[1], positions[2],
                                                              positions[3], ships_size[ship])
                    ships_placement[ship] = 1
                except BattleShipException as be:
                    print(be)
            self.print_grids('human', 'enemygrid')

    def __place_human_ships_brut(self):
        self.__game_service.human_player_add_ship('Battleship', 1, 5, 1, 8, 4)
        self.__game_service.human_player_add_ship('Cruiser', 4, 6, 4, 8, 3)
        self.__game_service.human_player_add_ship('Destroyer', 1, 1, 1, 2, 2)

    def __place_comp_ships_brut(self):
        self.__game_service.computer_player_add_ship('Battleship', 1, 3, 1, 6, 4)
        self.__game_service.computer_player_add_ship('Cruiser', 8, 5, 8, 7, 3)
        self.__game_service.computer_player_add_ship('Destroyer', 2, 4, 2, 5, 2)

    def run_game(self):
        self.__print_game_rules()
        self.__place_human_ships()
        self.__game_service.place_computer_ships()
        player = 'human'
        computer_tries = 0
        while True:
            try:
                print("It is " + player + '\'s turn.')
                if player == 'human':
                    self.print_grids(player, 'mygrid')
                    square_position = self.__read_square_position()
                    message = self.__game_service.human_turn(square_position[0], square_position[1])
                    player = 'computer'
                elif player == 'computer':
                    computer_tries += 1
                    message = self.__game_service.computer_turn()
                    player = 'human'
                print(message)
                if message.find('won') != -1:
                    break
            except ValueError as ve:
                print('Wrong row / column. Try again!')
            except BattleShipException as be:
                print(be)
