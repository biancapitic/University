import configparser
from domain.entities import Movie, Client, Rental
from repository.Repository import Repository, FileRepository, BinaryFileRepository
from exception.errors import MyAppError


class Settings:
    repository_type = ""
    movies_file = ""
    clients_file = ""
    rentals_file = ""

    @staticmethod
    def initialize():
        config = configparser.ConfigParser()
        config.read('settings.properties')

        Settings.repository_type = config.get('repository_config', 'repository')
        Settings.movies_file = config.get('movies_file_config', 'movies_file')
        Settings.clients_file = config.get('clients_file_config', 'clients_file')
        Settings.rentals_file = config.get('rentals_file_config', 'rentals_file')

    @staticmethod
    def initialize_movie_repository():
        if Settings.repository_type == 'memory':
            movie_repository = Repository()
        elif Settings.repository_type == 'file':
            movie_repository = FileRepository('movies.txt', Movie.read_movie, Movie.write_movie)
        elif Settings.repository_type == 'binaryfile':
            movie_repository = BinaryFileRepository('movies_binary.txt')
        return movie_repository

    @staticmethod
    def initialize_client_repository():
        if Settings.repository_type == 'memory':
            client_repository = Repository()
        elif Settings.repository_type == 'file':
            client_repository = FileRepository('clients.txt', Client.read_client, Client.write_client)
        elif Settings.repository_type == 'binaryfile':
            client_repository = BinaryFileRepository('clients_binary.txt')
        return client_repository

    @staticmethod
    def initialize_rental_repository():
        if Settings.repository_type == 'memory':
            rental_repository = Repository()
        elif Settings.repository_type == 'file':
            rental_repository = FileRepository('rentals.txt', Rental.read_rental, Rental.write_rental)
        elif Settings.repository_type == 'binaryfile':
            rental_repository = BinaryFileRepository('rentals_binary.txt')
        return rental_repository

    @staticmethod
    def default_repository_values(repository_type, movie_repository, client_repository, rental_repository):
        if repository_type in ['memory', 'binaryfile']:
            # 10 movies for the start of the app
            try:
                movie_repository.add_element(Movie(1, 'Nemo', 'fun', 'cartoon'))
                movie_repository.add_element(Movie(2, 'Cars', 'boys', 'cartoon'))
                movie_repository.add_element(Movie(3, 'Hobbit', 'great', 'SF'))
                movie_repository.add_element(Movie(4, 'Fast', 'cars', 'great'))
                movie_repository.add_element(Movie(5, 'Barbie', 'girls', 'cartoon'))
                movie_repository.add_element(Movie(6, 'Nature', 'real', 'documentary'))
                movie_repository.add_element(Movie(7, 'New', 'fun', 'comedy'))
                movie_repository.add_element(Movie(8, 'Stars', 'universe', 'documentary'))
                movie_repository.add_element(Movie(9, 'Sun', 'nature', 'documentary'))
                movie_repository.add_element(Movie(10, 'Tom', 'cat', 'cartoon'))

                # 7 clients for the start of the app
                client_repository.add_element(Client(1, 'Bianca'))
                client_repository.add_element(Client(2, 'Ana'))
                client_repository.add_element(Client(3, 'Ioana'))
                client_repository.add_element(Client(4, 'Adi'))
                client_repository.add_element(Client(5, 'Filip'))
                client_repository.add_element(Client(6, 'Manu'))
                client_repository.add_element(Client(7, 'Andreea'))

                # 10 rentals for the start of the app
                rental_repository.add_element(Rental(1, 1, 1, '20.11.2019', '30.11.2019', ''))
                rental_repository.add_element(Rental(2, 2, 2, '21.11.2019', '28.11.2019', ''))
                rental_repository.add_element(Rental(3, 3, 3, '10.11.2019', '20.11.2019', ''))
                rental_repository.add_element(Rental(4, 4, 4, '21.11.2019', '28.11.2019', '27.11.2019'))
                rental_repository.add_element(Rental(5, 5, 5, '01.11.2019', '23.11.2019', ''))
                rental_repository.add_element(Rental(6, 6, 1, '19.11.2019', '30.11.2019', ''))
                rental_repository.add_element(Rental(7, 7, 2, '15.11.2019', '18.11.2019', '20.11.2019'))
                rental_repository.add_element(Rental(8, 8, 7, '26.11.2019', '28.11.2019', ''))
                rental_repository.add_element(Rental(9, 7, 3, '25.11.2019', '30.11.2019', ''))
                rental_repository.add_element(Rental(10, 10, 5, '13.11.2019', '25.11.2019', ''))
            except MyAppError as e:
                pass
