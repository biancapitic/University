from services.services import MovieService
from services.services import ClientService
from services.services import RentalService
from UI.Console import UI
from settings import Settings

Settings.initialize()
movie_repository = Settings.initialize_movie_repository()
client_repository = Settings.initialize_client_repository()
rental_repository = Settings.initialize_rental_repository()
Settings.default_repository_values(Settings.repository_type, movie_repository, client_repository, rental_repository)

movie_service = MovieService(movie_repository)
client_service = ClientService(client_repository)
rental_service = RentalService(movie_repository, client_repository, rental_repository)

ui = UI(movie_service, client_service, rental_service)
ui.run_app()

