from Repository.repository import GameRepository
from Service.service import Service
from Console.Console import UI

repository = GameRepository()
service = Service(repository)
ui = UI(service)
ui.play_game()