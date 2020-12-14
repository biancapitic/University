from Validator.Validator import Validator


class Repository:
    def __init__(self, filename):
        self.__filename = filename
        self._sentences = []

    '''
        The function reads the sentences from the file.
    '''

    def __read_from_file(self):
        self._sentences = []
        with open(self.__filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    self._sentences.append(line.split(' '))

    '''
        The function writes in the file the current list of sentences.
    '''

    def __write_in_file(self):
        with open(self.__filename, 'w') as file:
            for sentence in self._sentences:
                line = ''
                for index in range(len(sentence) - 1):
                    line = line + sentence[index] + ' '
                line += sentence[-1] + '\n'
                file.write(line)

    '''
        The function adds a new sentence to the list and into the file.
    '''

    def add_sentence(self, sentence):
        self.__read_from_file()
        Validator.validate_sentence(self._sentences, sentence)
        self._sentences.append(sentence)
        self.__write_in_file()

    '''
        The function returns the list of sentences.
    '''

    def get_sentences(self):
        self.__read_from_file()
        return self._sentences
