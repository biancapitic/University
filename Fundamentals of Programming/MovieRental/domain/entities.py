class Movie:
    def __init__(self, Id, Title, Description, Genre):
        self.__id = Id
        self.__title = Title
        self.__description = Description
        self.__genre = Genre

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def genre(self):
        return self.__genre

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    def __str__(self):
        return 'ID: ' + str(self.__id) + ', TITLE: ' + self.__title + ', DESCRIPTION: ' + self.__description + ', GENRE: ' + self.__genre

    def get_attribute_value(self, attribute):
        if attribute == 'id':
            return self.id
        elif attribute == 'title':
            return  self.title
        elif attribute == 'description':
            return self.description
        elif attribute == 'genre':
            return self.genre

    @staticmethod
    def read_movie(line):
        attributes = line.split(',')
        return Movie(int(attributes[0]), attributes[1], attributes[2], attributes[3])

    @staticmethod
    def write_movie(movie):
        return str(movie.id) + ',' + movie.title + ',' + movie.description + ',' + movie.genre


class Client:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return 'ID: ' + str(self.__id ) + ', NAME: ' + self.__name

    def get_attribute_value(self, attribute):
        if attribute == 'id':
            return self.id
        elif attribute == 'name':
            return self.name

    @staticmethod
    def read_client(line):
        attributes = line.split(',')
        return Client(int(attributes[0]), attributes[1])

    @staticmethod
    def read_client_binary(client):
        return client

    @staticmethod
    def write_client(client):
        return str(client.id) + ',' + client.name

    @staticmethod
    def write_client_binary(client):
        return client

class Rental:

    def __init__(self, id, movie_id, client_id, rented_date, due_date, returned_date):
        self.__id = id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    @property
    def id(self):
        return self.__id

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, new_rented_date):
        self.__rented_date = new_rented_date

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, new_due_date):
        self.__due_date = new_due_date

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, new_returned_date):
        self.__returned_date = new_returned_date

    def __str__(self):
        return 'RENTAL_ID: ' + str(self.__id) + ', MOVIE_ID: ' + str(self.__movie_id) + ', CLIENT_ID: ' + str(self.__client_id) + '\n' \
               + 'RENTED_DATE: ' + self.__rented_date + ', DUE_DATE: ' + self.__due_date + ', RETURNED_DATE: '  + self.__returned_date

    def get_attribute_id(self, attribute_type):
        if attribute_type == 'movie':
            return self.movie_id
        elif attribute_type == 'client':
            return self.client_id
        elif attribute_type == 'rental':
            return self.id

    @staticmethod
    def read_rental(line):
        attributes = line.split(',')
        if attributes[5] == '\'\'':
            attributes[5] = ''
        return Rental(int(attributes[0]), int(attributes[1]), int(attributes[2]), attributes[3], attributes[4], attributes[5])

    @staticmethod
    def write_rental(rental):
        return str(rental.id) + ',' + str(rental.movie_id) + ',' + str(rental.client_id) + ',' + rental.rented_date + ',' \
               + rental.due_date + ',' + rental.returned_date
