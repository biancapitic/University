from Domain.entities import Player, Position, Grid
from Exceptions.exceptions import ValidatorException
from Service.player_service import PlayerService
from Service.computer_service import ComputerService

import unittest


class Tests(unittest.TestCase):
    def testPlaceShip_ValidPosition_ShipPlaced(self):
        player_grid = Grid()
        player_enemy_grid = Grid()
        player = Player(player_grid, player_enemy_grid)
        player_service = PlayerService(player)

        player_service.place_ship('Cruiser', 1, 1, 1, 3, 3)
        for column in range(1, 4):
            self.assertEqual(player.my_grid.grid[1][column], 'S')

    def testPlaceShip_InvalidPosition_ExceptionMessage(self):
        player_grid = Grid()
        player_enemy_grid = Grid()
        player = Player(player_grid, player_enemy_grid)
        player_service = PlayerService(player)

        with self.assertRaises(ValidatorException):
            player_service.place_ship('Cruiser', 1, 1, 1, 2, 3)

    def testGetShipHitName_SquarePosition_RightShipName(self):
        player_grid = Grid()
        player_enemy_grid = Grid()
        player = Player(player_grid, player_enemy_grid)
        player_service = PlayerService(player)

        player_service.place_ship('Cruiser', 1, 1, 1, 3, 3)
        player_service.place_ship('Battleship', 2, 1, 2, 4, 4)

        self.assertEqual(player_service.get_ship_hit_name(Position(2,2)), 'Battleship')

    def testGameOver_NotAllShipsSank_False(self):
        player_grid = Grid()
        player_enemy_grid = Grid()
        player = Player(player_grid, player_enemy_grid)
        player_service = PlayerService(player)

        player_service.place_ship('Cruiser', 1, 1, 1, 3, 3)
        player_service.place_ship('Battleship', 2, 1, 2, 4, 4)
        player_service.place_ship('Destroyer', 3, 4, 3, 5, 2)

        player.ships['Cruiser'].damage = 3
        player.ships['Battleship'].damage = 4
        self.assertEqual(player_service.game_over(), False)

    def testChooseSquare_HuntMode_GreatestProbabilitySquarePosition(self):
        player_grid = Grid()
        player_enemy_grid = Grid()
        player = Player(player_grid, player_enemy_grid)
        player_service = ComputerService(player)

        square_position = player_service.choose_square()
        self.assertEqual(square_position.row, 4)
        self.assertEqual(square_position.column, 5)


if __name__ == '__main__':
    unittest.main()
