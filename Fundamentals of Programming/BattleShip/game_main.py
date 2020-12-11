from Domain.entities import Grid, Player
from Service.player_service import PlayerService
from Service.computer_service import ComputerService
from Service.game_service import GameService
from Console.console import UI

human_grid = Grid()
human_enemy_grid = Grid()

computer_grid = Grid()
computer_enemy_grid = Grid()

human_player = Player(human_grid, human_enemy_grid)
human_player_service = PlayerService(human_player)

computer_player = Player(computer_grid, computer_enemy_grid)
computer_player_service = ComputerService(computer_player)

g = GameService(human_player_service, computer_player_service)

ui = UI(g)
ui.run_game()