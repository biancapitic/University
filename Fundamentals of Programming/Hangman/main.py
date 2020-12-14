from Repository.Repository import Repository
from Service.Service import GameService
from UI.Console import UI

sentences_repository = Repository('sentences.txt')
game_service = GameService(sentences_repository)
ui = UI(sentences_repository, game_service)
ui.run_app()
