# Kakuro-AI

Kakuro is a logic puzzle that is often referred to as a mathematical transliteration of the crossword. The puzzle is played in a grid of filled and barred cells, "black" and "white" respectively. The black cells contain a diagonal slash from upper-left to lower-right and a number in one or both halves, such that each horizontal entry has a number in the black half-cell to its immediate left and each vertical entry has a number in the black half-cell immediately above it. The objective of the puzzle is to insert a digit from 1 to 9 inclusive into each white cell such that the sum of the numbers in each entry matches the clue associated with it and that no digit is duplicated in any entry.

# Algorithms

There are four different puzzles to be solved and there have been 3 different algorithms to achieve that.
The algorithms are:

-BackTracking (BT)
-Forward Checking (FC)
-Maintaining Arc Consistency (MAC)

Those algorithms were forked by AIMA (https://github.com/aimacode/aima-python).

# Files

The file of my code is kakuro.py and all the rest are also from AIMA.

# Results

The time-table: 


          SIMPLE BACKTRACKING - BT   | FORWARD CHECKING - FC   |  MAINTAINING ARC CONSISTENCY - MAC 
KAKURO1           25 microsec              0,... microsec                     1 microsec

KAKURO2           2 microsec               0,... microsec                     1 microsec

KAKURO3          44431 microsec              4 microsec                       7 microsec

KAKURO4         1097825 microsec            21 microsec                       35 microsec

So, we notice that simple backtracking is by far the slowest algorithm, while FC and MAC have close times but obviously faster is FC. This result was expected because the FC and MAC are improvements  BT. 
