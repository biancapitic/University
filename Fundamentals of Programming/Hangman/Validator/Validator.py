from Exceptions.Errors import HangmanException


class Validator:

    @staticmethod
    # checks if a sentence is valid and if it can be added to the sentences list
    def validate_sentence(sentences_list, sentence):
        # sentence is a list of words
        if len(sentence) < 1:
            raise HangmanException("Validator Exception: The sentence is to short.")
        for word in sentence:
            if len(word) < 3:
                raise HangmanException("Validator Exception: A word must have minimum 3 letters.")
        for sentence_element in sentences_list:
            if sentence_element == sentence:
                raise HangmanException("Validator Exception: The sentence is already in the list.")
