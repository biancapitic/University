import copy
import pickle

from exception.errors import RepositoryError
from exception.errors import EOFBinaryError


class Repository:
    def __init__(self):
        self._elements = {}

    def get_element(self, id):
        try:
            return self._elements[id]
        except KeyError:
            raise RepositoryError('ID not existent')

    def add_element(self, new_element):
        try:
            if new_element.id in  self._elements.keys():
                raise RepositoryError('Id already exists.')
            self._elements[new_element.id] = new_element
        except AttributeError:
            raise RepositoryError('Element doesn\'t have id')

    def remove_element(self, id):
        try:
            if id in self._elements.keys():
                del self._elements[id]
            else:
                raise RepositoryError('Element with that id doesn\'t exist.')
        except KeyError:
            raise RepositoryError('Element with that id doesn\'t exist.')

    def update_element(self, id, attribute, new_value):
        if id in self._elements:
            updated_element = copy.deepcopy(self._elements[id])
            if hasattr(updated_element, attribute):
                setattr(updated_element, attribute, new_value)
                self.replace_object(id, updated_element)
            else:
                raise RepositoryError('Element with that id doesn\'t exist.')
        else:
            raise RepositoryError('Element with that id doesn\'t exist.')

    def search_element(self, attribute, searched_value):
        searched_elements = []
        try:
            if attribute == 'id':
                searched_value = int(searched_value)
                if searched_value in self._elements.keys():
                    searched_elements.append(self._elements[searched_value])
            else:
                # we convert the string that we are searching into a lower case string
                searched_value = searched_value.lower()
                for element in self._elements:
                    # we convert the string of the element into a lower case string
                    element_string = self._elements[element].get_attribute_value(attribute).lower()
                    if element_string == searched_value.lower() or element_string.find(searched_value) != -1:
                        searched_elements.append(self._elements[element])
            return searched_elements
        except ValueError as ve:
            raise RepositoryError(ve)

    @property
    def get_elements_list(self):
        return self._elements

    def replace_object(self, object_id, new_object):
        self._elements[object_id] = new_object


class FileRepository(Repository):
    def __init__(self, filename, read_element, write_element):
        self.__filename = filename
        self.__read_element = read_element
        self.__write_element = write_element
        Repository.__init__(self)

    def __read_from_file(self):
        self._elements = {}
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    element = self.__read_element(line)
                    self._elements[element.id] = element

    def __write_in_file(self):
        with open(self.__filename, 'w') as file:
            for entity in self._elements:
                line = self.__write_element(self._elements[entity])
                file.write(line)
                file.write('\n')

    def add_element(self, new_element):
        self.__read_from_file()
        Repository.add_element(self, new_element)
        self.__write_in_file()

    def get_element(self, id):
        self.__read_from_file()
        return Repository.get_element(self, id)

    def remove_element(self, id):
        self.__read_from_file()
        Repository.remove_element(self,id)
        self.__write_in_file()

    def update_element(self, id, attribute, new_value):
        self.__read_from_file()
        Repository.update_element(self, id, attribute, new_value)
        self.__write_in_file()

    def search_element(self, attribute, searched_value):
        self.__read_from_file()
        return Repository.search_element(self, attribute, searched_value)

    @property
    def get_elements_list(self):
        self.__read_from_file()
        return self._elements

    def replace_object(self, object_id, new_object):
        self.__read_from_file()
        Repository.replace_object(self, object_id, new_object)
        self.__write_in_file()


class BinaryFileRepository(FileRepository):
    def __init__(self, filename):
        self.__filename = filename
        Repository.__init__(self)

    def __read_from_file(self):
        self._elements = {}
        with open(self.__filename, "rb") as file:
            while True:
                try:
                    file_object = pickle.load(file)
                    self._elements[file_object.id] = file_object
                except EOFError:
                    break
        file.close()

    def __write_in_file(self):
        with open(self.__filename, "wb") as file:
            for entity in self._elements:
                pickle.dump(self._elements[entity], file)
        file.close()

    def add_element(self, new_element):
        self.__read_from_file()
        Repository.add_element(self, new_element)
        self.__write_in_file()


    def get_element(self, id):
        self.__read_from_file()
        return Repository.get_element(self, id)

    def remove_element(self, id):
        self.__read_from_file()
        Repository.remove_element(self,id)
        self.__write_in_file()

    def update_element(self, id, attribute, new_value):
        self.__read_from_file()
        Repository.update_element(self, id, attribute, new_value)
        self.__write_in_file()

    def search_element(self, attribute, searched_value):
        self.__read_from_file()
        return Repository.search_element(self, attribute, searched_value)

    @property
    def get_elements_list(self):
        self.__read_from_file()
        return self._elements

    def replace_object(self, object_id, new_object):
        self.__read_from_file()
        Repository.replace_object(self, object_id, new_object)
        self.__write_in_file()

    def print_all(self):
        print("=============")
        self.__read_from_file()
        for ob in self._elements:
            print(self._elements[ob])