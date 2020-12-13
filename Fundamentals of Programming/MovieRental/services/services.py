from datetime import datetime
from domain.entities import Movie
from domain.entities import Client
from domain.entities import Rental
from validation.validators import MovieValidator
from validation.validators import GeneralValidator
from validation.validators import ClientValidator
from validation.validators import RentalValidator
from exception.errors import RentalError, MyAppError


class MovieService:
    def __init__(self, movie_repository):
        self.__repository = movie_repository
        self.__movie_validator = MovieValidator()
        self.__general_validator = GeneralValidator()

    def add_movie(self, id, title, descripton, genre):
        new_element = Movie(id, title, descripton, genre)
        self.__movie_validator.ValidateId(new_element.id)
        self.__repository.add_element(new_element)

    def remove_by_id(self, id):
        self.__movie_validator.ValidateId(id)
        self.__repository.remove_element(id)

    def update_movie_parameters(self, id, attribute, new_value):
        self.__movie_validator.ValidateId(id)
        self.__repository.update_element(id, attribute, new_value)

    def get_list_of_movies(self):
        return self.__repository.get_elements_list

    def search_for_elements(self, attribute, value):
        self.__movie_validator.ValidateAttribute(attribute)
        if attribute == 'id' and type(value) != int:
            raise MyAppError('Id must be an integer.')
        return self.__repository.search_element(attribute, value)

    def replace_element_with_id_given(self, id, new_element):
        self.__repository.replace_object(id, new_element)

    def get_element_by_id(self, id):
        return self.__repository.get_elements_list[id]


class ClientService:
    def __init__(self, client_repository):
        self.__repository = client_repository
        self.__client_validator = ClientValidator()
        self.__general_validator = GeneralValidator()

    def add_client(self, id, name):
        new_element = Client(id, name)
        self.__client_validator.ValidateId(id)
        self.__repository.add_element(new_element)

    def remove_by_id(self, id):
        self.__client_validator.ValidateId(id)
        self.__repository.remove_element(id)

    def update_client_parameters(self, id, attribute, new_value):
        self.__client_validator.ValidateId(id)
        self.__repository.update_element(id, attribute, new_value)

    def get_list_of_clients(self):
        return self.__repository.get_elements_list

    def search_for_elements(self, attribute, value):
        self.__client_validator.ValidateAttribute(attribute)
        if attribute == 'id' and type(value) != int:
            raise MyAppError('Id must be an integer.')
        return self.__repository.search_element(attribute, value)

    def replace_element_with_id_given(self, id, new_element):
        self.__repository.replace_object(id, new_element)

    def get_element_by_id(self, id):
        return self.__repository.get_elements_list[id]


class RentalService:
    def __init__(self, movie_repository, client_repository, rental_repository):
        self.__movie_repository = movie_repository
        self.__client_repository = client_repository
        self.__rental_repository = rental_repository
        self.__general_validator = GeneralValidator()
        self.__rental_validator = RentalValidator()

    def check_if_returned_date_greater(self, due_date, returned_date):
        '''
        Checks if returned_date is greater than due_date.
        '''
        # due_date = [day, month, year], returned_date = [day, month, year]

        # if year of returned_date is greater than year of the due_date
        if due_date[2] < returned_date[2]:
            return False

        # if the year is the same but the month of the returned date is greater than due_date's month
        if due_date[2] == returned_date[2] and due_date[1] < returned_date[1]:
            return False

        # if the year and month are the same but the day of the returned_date is greater than due_date's day
        if due_date[2] == returned_date[2] and due_date[1] == returned_date[1] and due_date[0] < returned_date[0]:
            return False
        # Any other case means that returned_date is smaller than due_date
        return True

    def convert_date_values_to_an_int_list(self, date_string):
        # date_string = [day.month.year]
        date_integers = []
        #day
        if date_string[0] == '0':
            date_integers.append(int(date_string[1]))
        else:
            date_integers.append(int(date_string[0:2]))

        #month
        if date_string[3] == '0':
            date_integers.append(int(date_string[4]))
        else:
            date_integers.append(int(date_string[3:5]))

        #year
        date_integers.append(int(date_string[6:]))
        return date_integers

    def if_client_has_passed_returned_dates_for_movies(self, id_client):
        '''
        It checks if the client from id_client has any movies where he passed over his due_date and returned it later,
        returns: True, if the client has any movie that he has rented and returned it later than he should
                 False, otherwise
        '''
        rentals = self.__rental_repository.get_elements_list
        for rental in rentals:
            if rentals[rental].client_id == id_client:
                if not rentals[rental].returned_date == '':
                    due_date = self.convert_date_values_to_an_int_list(rentals[rental].due_date)
                    returned_date = self.convert_date_values_to_an_int_list(rentals[rental].returned_date)
                    if not self.check_if_returned_date_greater(due_date, returned_date):
                        return True
        return False

    def check_if_movie_available(self, movie_id):
        # check if the movie is rented right now or not
        rentals = self.__rental_repository.get_elements_list
        for rental in rentals:
            if rentals[rental].movie_id == movie_id:
                if rentals[rental].returned_date == '':
                    return False

        # check if the movie exists in the movies list but was never rented until now
        movies = self.__movie_repository.get_elements_list
        for movie in movies:
            if movies[movie].id == movie_id:
                return True
        return False

    def add_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date, operation_type):
        # validate data
        self.__general_validator.IdExists(rental_id, self.__rental_repository.get_elements_list)
        self.__general_validator.IdFound(movie_id, self.__movie_repository.get_elements_list)
        self.__general_validator.IdFound(client_id, self.__client_repository.get_elements_list)
        self.__rental_validator.ValidateDate(due_date)
        self.__rental_validator.ValidateDate(rented_date)

        if not self.check_if_returned_date_greater(self.convert_date_values_to_an_int_list(due_date), self.convert_date_values_to_an_int_list(rented_date)):
            raise RentalError('The due date is wrong.')
        # check if we can create and add the Rental
        if not self.if_client_has_passed_returned_dates_for_movies(client_id) or operation_type == 'undo':
            if self.check_if_movie_available(movie_id) or operation_type == 'undo': # or returned_date != '':
                new_element = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
                self.__rental_repository.add_element(new_element)
            else:
                raise RentalError('Movie is not available.')
        else:
            raise RentalError('The client has rented movies that passed their due date for return.')

    def get_list_of_rentals(self):
        return self.__rental_repository.get_elements_list

    def return_movie(self, movie_id, new_returned_date):
        self.__general_validator.IdFound(movie_id, self.__movie_repository.get_elements_list)
        rentals = self.__rental_repository.get_elements_list
        self.__rental_validator.ValidateDate(new_returned_date)
        found_counter = 0
        for rental in rentals:
            if rentals[rental].movie_id == movie_id:
                if rentals[rental].returned_date == '':
                    found_counter += 1
                    self.__rental_repository.update_element(rental, 'returned_date', new_returned_date)
                    return rentals[rental].id
        if found_counter == 0:
            raise RentalError('The movie can\'t be returned.')

    def number_rented_days(self, rental):
        if rental.returned_date != '':
            total_days = (datetime.strptime(rental.returned_date, '%d.%m.%Y') - datetime.strptime(rental.rented_date, '%d.%m.%Y')).days
        else:
            pass
            total_days = (datetime.today() - datetime.strptime(rental.rented_date, '%d.%m.%Y')).days
        return total_days

    def check_entity_in_list(self, id_entity, rented_days_list):
        for element in rented_days_list:
            if element[0] == id_entity:
                return rented_days_list.index(element)
        return -1

    def get_sorted_list_of_entities(self, entities_list, entity_type):
        ordered_entities_list = []
        rentals = self.__rental_repository.get_elements_list
        if not rentals:
            raise RentalError('There are no rentals.')
        for element in rentals:
            rented_days = self.number_rented_days(rentals[element])
            entity_list_position = self.check_entity_in_list(rentals[element].get_attribute_id(entity_type), ordered_entities_list)
            if entity_list_position == -1:
                ordered_entities_list.append([rentals[element].get_attribute_id(entity_type), rented_days])
            else:
                ordered_entities_list[entity_list_position][1] += rented_days
        ordered_entities_list.sort(key=lambda x: x[1], reverse=True)
        for entity in entities_list:
            if self.check_entity_in_list(entities_list[entity].id, ordered_entities_list) == -1:
                ordered_entities_list.append([entities_list[entity].id, 0])
        return ordered_entities_list

    def most_rented_movies(self):
        movies = self.__movie_repository.get_elements_list
        movies_ordered_list = self.get_sorted_list_of_entities(movies, 'movie')
        return movies_ordered_list

    def most_active_clients(self):
        clients = self.__client_repository.get_elements_list
        clients_ordered_list = self.get_sorted_list_of_entities(clients, 'client')
        return clients_ordered_list

    def days_passed_due_date(self, rental):
        return (datetime.today() - datetime.strptime(rental.due_date, '%d.%m.%Y')).days

    def late_rentals(self):
        ordered_passed_dates_movies = []
        rentals = self.__rental_repository.get_elements_list
        if not rentals:
            raise RentalError('There are no rentals.')
        for element in rentals:
            if rentals[element].returned_date == '' and datetime.strptime(rentals[element].due_date, '%d.%m.%Y') < datetime.today():
                days_passed = self.days_passed_due_date(rentals[element])
                ordered_passed_dates_movies.append([rentals[element].movie_id, days_passed])
        ordered_passed_dates_movies.sort(key=lambda x: x[1], reverse=True)
        return ordered_passed_dates_movies

    def check_entity_id_in_rentals(self, entity_type, entity_id):
        rentals_list = self.__rental_repository.get_elements_list
        rentals_with_entity_id = []
        for rental in rentals_list:
            if entity_type == 'movie' and rentals_list[rental].movie_id == entity_id or entity_type == 'client' and rentals_list[rental].client_id == entity_id:
                rentals_with_entity_id.append(rentals_list[rental].id)
        return rentals_with_entity_id

    def remove_multiple_entities(self, rentals_id_list):
        for rental in rentals_id_list:
            self.remove_by_id(rental)

    def remove_by_id(self, id):
        self.__rental_validator.ValidateId(id)
        self.__rental_repository.remove_element(id)

    def get_list_of_certain_rentals(self, renatls_id):
        needed_rentals_list = []
        for id in renatls_id:
            needed_rentals_list.append(self.__rental_repository.get_element(id))
        return needed_rentals_list

    def get_element_by_id(self, id):
        return self.__rental_repository.get_elements_list[id]

    def replace_element_with_id_given(self, id, new_element):
        self.__rental_repository.replace_object(id, new_element)