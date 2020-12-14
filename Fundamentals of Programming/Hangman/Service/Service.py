from Domain.entities import Sentence
from random import randrange


class GameService:
    def __init__(self, sentences_repository):
        self._chosen_sentence = None
        self._sentences_repository = sentences_repository
        self._hangman_original_word = ["h", "a", "n", "g", "m", "a", "n"]
        self._hangman_game_word = ""
        self._chosen_letters = []

    '''
        The function returns the chosen sentence, that means the sentence which the player is trying to guess.
    '''
    def get_chosen_sentence(self):
        return self._chosen_sentence.sentence_hangman_style()

    '''
        The function returns the word "hangman" but completed with the number of letters equal to the number 
        of mistakes of the user.
    '''
    def get_hangman_game_word(self):
        return self._hangman_game_word

    '''
        The function adds a new sentence to the sentences list. 
    '''
    def add_sentence(self, sentence):
        self._sentences_repository.add_sentence(sentence)

    '''
        The function chooses randomly a sentence form the sentences list, which the player has to guess.
    '''
    def choose_sentence(self):
        list_of_sentences = self._sentences_repository.get_sentences()
        sentence_index = randrange(0, len(list_of_sentences))
        self._chosen_sentence = Sentence(list_of_sentences[sentence_index])

    '''
        The function adds a letter to complete the hangman_game_word, it means that the player chosed a wrong letter.
    '''
    def _computer_turn(self):
        self._hangman_game_word += self._hangman_original_word.pop(0)

    '''
        The function checks if the game is over or not. It returns an appropriate message.
    '''
    def check_if_game_over(self):
        if self._hangman_game_word == "hangman":
            return "computer"
        if self._chosen_sentence.check_sentence_status() is True:
            return "human"
        return "continue"

    '''
        The function checks if the letter chosen by the player it's ok or not and makes changes in conformity with that.
        If the game is over it returns the appropriate message.
    '''
    def play_game(self, chosen_letter):

        if chosen_letter in self._chosen_letters:
            self._computer_turn()
        else:
            if self._chosen_sentence.check_if_letter_in_sentence(chosen_letter):
                self._chosen_sentence.change_status_of_some_letter(chosen_letter)
            else:
                self._computer_turn()
        message = self.check_if_game_over()
        if message == "human":
            return "YOU WON!"
        elif message == "computer":
            return "YOU LOST!"
        else:
            return "continue"
