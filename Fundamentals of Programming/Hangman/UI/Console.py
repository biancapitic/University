from Exceptions.Errors import HangmanException


class UI:
    def __init__(self, sentences_repository, game_service):
        self._sentences_repository = sentences_repository
        self._game_service = game_service

    def __read_sentence(self):
        sentence = input("Enter sentence: ")
        sentence = sentence.strip()
        sentence = sentence.split(' ')
        print(sentence)
        self._game_service.add_sentence(sentence)

    def __play(self):
            self._game_service.choose_sentence()
            while True:
                try:
                    hang_word = self._game_service.get_hangman_game_word()
                    sentence = self._game_service.get_chosen_sentence()
                    if not hang_word:
                        print(sentence)
                    else:
                        print(sentence + " - " + hang_word)
                    letter = input("Enter letter: ")
                    message = self._game_service.play_game(letter)
                    if message != "continue":
                        print(message)
                        break
                except HangmanException as he:
                    print(he)

    def run_app(self):
        while True:
            print("0: Stop app.\n"
                  "1: Add a new sentence to the sentences list.\n"
                  "2: Play the game.\n")
            try:
                command = int(input("Enter command: "))
                if command == 0:
                    break
                if command == 1:
                    self.__read_sentence()
                else:
                    self.__play()
                    if self._game_service.get_hangman_game_word() == 'hangman':
                        break
            except ValueError as ve:
                print("Wrong command!")
            except HangmanException as he:
                print(he)

