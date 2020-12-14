import unittest
from Domain.entities import Sentence
from Repository.Repository import Repository
from Service.Service import GameService

class MyTestCase(unittest.TestCase):
    def testCheckIfLetterInSentence_ValidLetter_True(self):
        sentence = Sentence(['ana', 'are'])
        self.assertEqual(sentence.check_if_letter_in_sentence('a'), True)

    def testChangeStatusOfSOmeLetter_ValidLetter_StatusChanged(self):
        sentence = Sentence(['ana', 'are'])
        sentence.change_status_of_some_letter('r')
        self.assertEqual(sentence.get_sentence_status()[1][1], 1)

    def testSentenceStatus_False(self):
        sentence = Sentence(['ana', 'are'])
        self.assertEqual(sentence.check_sentence_status(), False)

    def testAddSentence_ValidSentence_SentenceAdded(self):
        sentences_repository = Repository('sentences.txt')
        game_service = GameService(sentences_repository)

        game_service.add_sentence(["batman is on duty"])
        self.assertEqual(["batman is on duty"] in sentences_repository.get_sentences(), True)

    def testCheckIfGameOver_GameNotOver_continue(self):
        sentences_repository = Repository('sentences.txt')
        game_service = GameService(sentences_repository)
        game_service.choose_sentence()

        self.assertEqual(game_service.check_if_game_over(), 'continue')

    def testComputerTurn_AddsALetterToHangWord(self):
        sentences_repository = Repository('sentences.txt')
        game_service = GameService(sentences_repository)
        game_service.choose_sentence()

        game_service._computer_turn()
        self.assertEqual(game_service.get_hangman_game_word(), "h")