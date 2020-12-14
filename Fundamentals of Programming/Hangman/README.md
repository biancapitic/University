# Hangman

This is a Python implementation of the well known **hangman** game.
The application lets you to:
- add a new sentence(it must have at least a word with at least 3 letters) that will be saved in the sentences text file of the project;
- play the game:
  - in the first round the computer shows the first and the last letter for each word and also all their appearences in the sentence;
  - the computer shows you on each round: 
    - the sentence with all its guessed letters;
    - the "hangman" word - each wrong guesed letter adds a letter to the "hangman" word;
  - when the "hangman" word has all its letters the user loses;
- stop the application;

It is a console based application that has a layered architecture and uses PyUnit tests.
