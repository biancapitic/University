import copy


class Sentence:
    def __init__(self, sentence):
        self._sentence = sentence
        self._sentence_status = []
        self.__init_sentence(sentence)
    '''
    The function initializes the sentence_status list. The sentence_status list is a list which contains a 0 or a 1 
    for each letter from the sentence; 0 if the letter wan't discovered yet, 1 otherwise
    '''
    def __init_sentence(self, sentence):
        appeared_letters = []
        for word in sentence:
            word_status = []
            for letter in word:
                if word[0] == letter or word[-1] == letter:
                    word_status.append(1)
                    if letter not in appeared_letters:
                        appeared_letters.append(letter)
                else:
                    word_status.append(0)
            self._sentence_status.append(copy.deepcopy(word_status))
        for word_index in range(0, len(self._sentence)):
            for letter_index in range(0, len(self._sentence[word_index])):
                if self._sentence[word_index][letter_index] in appeared_letters:
                    self._sentence_status[word_index][letter_index] = 1
    '''
        Function checks if a letter is in the sentence. Returns True if the letter is in the sentence and False otherwise.
    '''

    def check_if_letter_in_sentence(self, letter):
        for word in self._sentence:
            if letter in word:
                return True
        return False

    def get_sentence(self):
        return self._sentence

    def get_sentence_status(self):
        return self._sentence_status

    '''
     Function returns the sentence in the hangman game format of the sentence which has to be printed on the screen.
    '''
    def sentence_hangman_style(self):
        sentence = ''
        for word_index in range(0, len(self._sentence)):
            for letter_index in range(0, len(self._sentence[word_index])):
                if self._sentence_status[word_index][letter_index] == 1:
                    sentence += self._sentence[word_index][letter_index]
                else:
                    sentence += "_"
            sentence += ' '
        return sentence

    '''
        The function puts the value 1 in the sentence_status list wherever at the same position in the sentence is the
        same letter as the one given as a parameter.
    '''
    def change_status_of_some_letter(self, letter):
        for word_index in range(0, len(self._sentence)):
            for letter_index in range(0, len(self._sentence[word_index])):
                if self._sentence[word_index][letter_index] == letter:
                    self._sentence_status[word_index][letter_index] = 1

    '''
        The function checks if the sentence is fully guessed or not. If in the status list are only values of 1
        it means that the sentence is fully guessed.
    '''

    def check_sentence_status(self):
        find = False
        for word_index in range(0, len(self._sentence)):
            for letter_index in range(0, len(self._sentence[word_index])):
                if self._sentence_status[word_index][letter_index] == 0:
                    find = True
        if find:
            return False
        return True
