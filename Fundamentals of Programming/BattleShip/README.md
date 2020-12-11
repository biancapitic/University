# BATTLESHIP

This project is my implementation for the well known **Battleship** game.
The game is played with only 3 ships(Cruiser, Battleship, Destroyer) for each player.
You are playing against the computer.

## Computer strategy
Computer has two modes of playing:
### 1. Hunt mode
  This means that he chooses the square that will be targeted this time depending of the square's probability value. 
  In Hunt mode he does 3 things: -> reinitialize's the probability grid with 0's.
                                 -> update's the probability grid with values depending on enemy grid.
                                 -> He gets the position of the square that has the bigger probability.
  The probability grid is a map with all the squares from the table. Each position has an integer value that is computed based on how probable is that an enemy ship is placed       there.

### 2. Track mode
  Track mode means that in the previous round he had a HIT. So he found a ship. 
  There is a stack in which we have the positions of the neighbour's squares of the square that was HIT. He takes the last element from this stack and considers it as the current   targeted square.
