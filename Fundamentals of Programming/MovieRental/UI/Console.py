from exception.errors import ValidatorError, RepositoryError, RentalError, EmptyError, MyAppError, EOFBinaryError
from services.undo_redo_handler import UndoHandler
from services.undo_redo import UndoRedoManager
import copy

class UI():

    def __init__(self, movieService, clientService, rentalService):
        self.__movie_service = movieService
        self.__client_service = clientService
        self.__rental_service = rentalService
        self.__commands_requirements = {'1': "Enter: <movieId>, <title>, <description>, <genre>.",
                                        '3': "Enter: <movieId>.",
                                        '4': "Enter: <movieId>.",
                                        '5': "Enter: <clientId>, <name>.",
                                        '7': "Enter: <clientId>.",
                                        '8': "Enter: <clientId>, <new_name>.",
                                        '11': "Enter: <movieId>.",
                                        '12': "Enter:\n"
                                              "1: client\n"
                                              "2: movie\n"}
        self.__commands = {'1': self.__ui_add_movie,
                           '2': self.__ui_list_all_movies,
                           '3': self.__ui_remove_movie,
                           '4': self.__ui_update_movie,
                           '5': self.__ui_add_client,
                           '6': self.__ui_list_all_clients,
                           '7': self.__ui_remove_client,
                           '8': self.__ui_update_client,
                           '9': self.__ui_rent_a_movie,
                           '10': self.__ui_list_all_rentals,
                           '11': self.__ui_return_movie,
                           '12': self.__ui_search_for_clients_or_movies,
                           '13': self.__ui_most_rented_movies,
                           '14': self.__ui_most_active_clients,
                           '15': self.__ui_late_rentals,
                           '16': self.__ui_undo_last_operation,
                           '17': self.__ui_redo_last_operation}

    def __ui_add_movie(self, parameters):
        if len(parameters) != 4:
            print("It requires 4 parameters.")
        else:
            try:
                id = int(parameters[0])
                title = parameters[1]
                description = parameters[2]
                genre = parameters[3]
                self.__movie_service.add_movie(id, title, description, genre)
                UndoRedoManager.add_undo_operation([self.__movie_service], UndoHandler.ADD_ENTITY_HANDLER, self.__movie_service.get_element_by_id(id))
            except ValueError:
                print('The id has to be an integer.')

    def __ui_list_all_movies(self, parameters):
        if len(parameters) == 0:
            movies = self.__movie_service.get_list_of_movies()
            if not movies:
                print("Empty list.")
            else:
                for movie in movies:
                    print(movies[movie])
        else:
            print("Wrong command.")

    def __ui_remove_movie(self, parameters):
        if len(parameters) == 1:
            try:
                id = int(parameters[0])
                rentals_id = self.__rental_service.check_entity_id_in_rentals('movie', id)
                if len(rentals_id) > 0:
                    UndoRedoManager.add_undo_operation([self.__movie_service, self.__rental_service], UndoHandler.DELETE_ENTITY_HANDLER,
                                          self.__movie_service.get_list_of_movies()[id],
                                          self.__rental_service.get_list_of_certain_rentals(rentals_id))
                    self.__rental_service.remove_multiple_entities(rentals_id)
                else:
                    UndoRedoManager.add_undo_operation([self.__movie_service], UndoHandler.DELETE_ENTITY_HANDLER,
                                              self.__movie_service.get_list_of_movies()[id])
                self.__movie_service.remove_by_id(id)
            except ValueError:
                print('Id must be an integer.')
        else:
            print('You have to enter one parameter.')

    def __ui_update_movie(self, parameters):
        if len(parameters) == 1:
            try:
                id = int(parameters[0])
                print("What parameter from the movie you want to update?\n"
                      "Options: \n"
                      "1: Title.\n"
                      "2: Description.\n"
                      "3: Genre.\n")
                attribute = ''
                new_value = ''
                command = input("Enter command: ")
                if command == '1':
                    new_value = input("Enter title: ")
                    attribute = 'title'
                elif command == '2':
                    new_value = input("Enter description: ")
                    attribute = 'description'
                elif command == '3':
                    new_value = input('Enter genre: ')
                    attribute = 'genre'
                if command in ['1', '2', '3']:
                    UndoRedoManager.add_undo_operation(self.__movie_service, UndoHandler.UPDATE_ENTITY_HANDLER,
                                                       copy.deepcopy(self.__movie_service.get_element_by_id(id)), id)
                    self.__movie_service.update_movie_parameters(id, attribute, new_value)
                else:
                    print("Wrong command.")
            except ValueError:
                print('ID must be a positive integer.')
        else:
            print('You have to enter the movie ID after command.')

    def  __ui_add_client(self, parameters):
        if len(parameters) != 2:
            print("It requires 2 parameters.")
        else:
            try:
                id = int(parameters[0])
                name = parameters[1]
                self.__client_service.add_client(id, name)
                UndoRedoManager.add_undo_operation([self.__client_service], UndoHandler.ADD_ENTITY_HANDLER,
                                                   self.__client_service.get_element_by_id(id))
            except ValueError:
                print('The id has to be an integer.')

    def __ui_list_all_clients(self, parameters):
        if len(parameters) == 0:
            clients = self.__client_service.get_list_of_clients()
            if not clients:
                print("Empty list.")
            else:
                for client in clients:
                    print(clients[client])
        else:
            print("Wrong command.")

    def __ui_remove_client(self, parameters):
        if len(parameters) == 1:
            id = int(parameters[0])
            rentals_id = self.__rental_service.check_entity_id_in_rentals('client', id)
            if len(rentals_id):
                UndoRedoManager.add_undo_operation([self.__client_service, self.__rental_service], UndoHandler.DELETE_ENTITY_HANDLER,
                                          self.__client_service.get_list_of_clients()[id],
                                          self.__rental_service.get_list_of_certain_rentals(rentals_id))
                self.__rental_service.remove_multiple_entities(rentals_id)
            else:
                UndoRedoManager.add_undo_operation([self.__client_service], UndoHandler.DELETE_ENTITY_HANDLER,
                                          self.__client_service.get_list_of_clients()[id])
            self.__client_service.remove_by_id(id)
        else:
            print('You have to enter one parameter.')

    def __ui_update_client(self, parameters):
        if len(parameters) == 2:
            try:
                id = int(parameters[0])
                attribute = 'name'
                new_name = parameters[1]
                UndoRedoManager.add_undo_operation(self.__client_service, UndoHandler.UPDATE_ENTITY_HANDLER,
                                                   self.__client_service.get_element_by_id(id), id)
                self.__client_service.update_client_parameters(id, attribute, new_name)
            except ValueError:
                print('ID must be a positive integer.')
        else:
            print('You have to enter the client ID after command.')

    def __ui_rent_a_movie(self, parameters):
        if len(parameters) == 0:
            try:
                rental_id = int(input("Enter id for rental: "))
                movie_id = int(input("Enter movie id: "))
                client_id = int(input("Enter client id: "))
                rented_date = input("Enter the rented_date (format: day.month.year, year > 1000): ")
                due_date = input("Enter the due_date (format: day.month.year, year > 1000): ")
                self.__rental_service.add_rental(rental_id, movie_id, client_id, rented_date, due_date, '', 'normal')
                UndoRedoManager.add_undo_operation([self.__rental_service], UndoHandler.ADD_ENTITY_HANDLER,
                                                   self.__rental_service.get_element_by_id(rental_id))
                print('The movie was rented with success.')
            except ValueError:
                print('Id\'s must be integers.')
            except RentalError as re:
                print(re)
            except ValidatorError as ve:
                print(ve)
            except IndexError as ie:
                print('The format of the date was not ok.')

    def __ui_list_all_rentals(self, parameters):
        if len(parameters) == 0:
            rentals = self.__rental_service.get_list_of_rentals()
            if not rentals:
               print("Empty list.")
            else:
                for rental in rentals:
                    print(rentals[rental])
                    print()
        else:
            print('Wrong command.')

    def __ui_return_movie(self, parameters):
        if len(parameters) == 1:
            try:
                movie_id = int(parameters[0])
                new_returned_date = input("Enter the returned_date (format: day.month.year, year > 1000): ")
                rental_id = self.__rental_service.return_movie(movie_id, new_returned_date)
                UndoRedoManager.add_undo_operation(self.__rental_service, UndoHandler.RETURN_MOVIE_HANDLER, rental_id)
                print('The movie was returned with success.')
            except ValueError:
                print('Id must be an integer.')
            except ValidatorError as ve:
                print(ve)
        else:
            print('Wrong command.')

    def __ui_search_for_clients_or_movies(self, parameters):
        client_fields = {'1':'id', '2':'name'}
        movie_fields = {'1': 'id', '2': 'title', '3' :'description', '4':'genre'}
        try:
            returned_elements = ''
            if parameters[0] not in ['1', '2']:
                print("Wrong command.")
            else:
                if parameters[0] == '1':
                    print("Search for clients using one of these fields:\n"
                          "1: id\n"
                        "2: name\n")
                    choice = input("Enter field: ")
                    if choice not in ['1', '2']:
                        print ("Option does not exist.")
                    else:
                        attribute = client_fields[choice]
                        value = input("Enter the value that you want to do the search: ")
                        returned_elements = self.__client_service.search_for_elements(attribute, value)
                elif parameters[0] == '2':
                    print("Search for clients using one of these fields:\n"
                          "1: id\n"
                        "2: title\n"
                        "3: description\n"
                        "4: genre\n")
                    choice = input("Enter field: ")
                    if choice not in ['1', '2', '3', '4']:
                        print("Option does not exist.")
                    else:
                        attribute = movie_fields[choice]
                        value = input("Enter the value that you want to do the search:")
                        returned_elements = self.__movie_service.search_for_elements(attribute, value)
                if not returned_elements:
                    print("No element containing that value in the filed that you searched exists.")
                else:
                    for element in returned_elements:
                        print(element)
        except MyAppError as e:
            print(e)

    def __ui_most_rented_movies(self, parameters):
        if len(parameters) != 0:
            print('Wrong command.')
        else:
            ordered_rented_movies_list = self.__rental_service.most_rented_movies()
            if not ordered_rented_movies_list:
                print('There are no movies in the movies list.')
            else:
                try:
                    movies_list = self.__movie_service.get_list_of_movies()
                    for movie in ordered_rented_movies_list:
                        print("Total rented days: " + str(movie[1]))
                        print(movies_list[movie[0]])
                        print()
                except RentalError as re:
                    print(re)

    def __ui_most_active_clients(self, parameters):
        if len(parameters) != 0:
            print('Wrong command.')
        else:
            ordered_clients_list = self.__rental_service.most_active_clients()
            if not ordered_clients_list:
                print('There are no clients in the clients list.')
            else:
                try:
                    clients_list = self.__client_service.get_list_of_clients()
                    for client in ordered_clients_list:
                        print("Total rented days: " + str(client[1]))
                        print(clients_list[client[0]])
                        print()
                except RentalError as re:
                    print(re)

    def __ui_late_rentals(self, parameters):
        if len(parameters) != 0:
            print('Wrong command.')
        else:
            ordered_late_rentals_list = self.__rental_service.late_rentals()
            if not ordered_late_rentals_list:
                print('There are no movies in the movies list.')
            else:
                try:
                    movies_list = self.__movie_service.get_list_of_movies()
                    for movie in ordered_late_rentals_list:
                        print('Total of passed days: ' + str(movie[1]))
                        print(movies_list[movie[0]])
                        print()
                except RentalError as re:
                    print(re)

    def  __ui_undo_last_operation(self, parameters):
        if len(parameters) != 0:
            print('Wrong command.')
        else:
            try:
                UndoRedoManager.undo()
            except EmptyError as e:
                print(e)

    def __ui_redo_last_operation(self, parameters):
        if len(parameters) != 0:
            print('Wrong command..')
        else:
            try:
                UndoRedoManager.redo()
            except EmptyError as e:
                print(e)

    def print_commands(self):
        print("Options: \n"
              "0:     Stop app.\n" 
              "1:     Add a movie.\n"
              "2:     List all movies.\n"
              "3:     Remove movie.\n"
              "4:     Update movie.\n"
              "5:     Add a client.\n"
              "6:     List all clients.\n"
              "7:     Remove client.\n"
              "8:     Update client.\n"
              "9:     Rent a movie.\n"
              "10:    List all rentals.\n"
              "11:    Return movie: <movieId>.\n"
              "12:    Search for a movie / client using any of their fields.\n"
              "13:    Most rented movies list.\n"
              "14:    Most active clients list.\n"
              "15:    Late rentals (shows all the movies that are still not returned, in desc order by nr of days paseed).\n"
              "16:    Undo last operation.\n"
              "17:    Redo last operation.\n")


    def run_app(self):
        while True:
            self.print_commands()
            command = input("Enter command: ")
            if command == '0':
                break
            command_name = command
            if command in self.__commands_requirements.keys():
                print(self.__commands_requirements[command])
                command = input("Enter requirements: ")
                command = command.replace(',', '')
                command = command.strip()
            if command == "":
                print("Enter a valid command.")
            else:
                if command_name not in ['2', '6', '9', '10', '13', '14', '15', '16', '17']:
                    command = command.split()
                    parameters = command[0:]
                else:
                    parameters = ''
                if command_name in self.__commands:
                    try:
                        self.__commands[command_name](parameters)
                    except MyAppError as e:
                        print(e)
                else:
                    print("Wrong command! Try again.")