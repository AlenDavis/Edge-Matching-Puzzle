# Edge-Matching-Puzzle
Puzzle

For both the algorithms the input is split into three arrays,  each representing corner, middle and edge pieces. 

GA
--
During initialization of GA, the pieces are randomly chosen from the input sure, wherein each of the pieces is selected from the respective array.

Each of the individuals has three arrays to represent the corner, side, and middle pieces along with a fitness score as its attributes.

Selection used is the basic tournament selection.

The mutation and crossover operations are applied separately for corners, sides and middle arrays.

The better off springs replace the worst performing individuals in the previous generation.

To run the code, update the input csv file in the main program "GA_main.py"

MCTS
----
In MCTS,  begins with the root node, which is an empty puzzle. Then place each piece by considering the edge with the edge of its neighbors along with its position. After placing each possible piece at a position in the puzzle, a complete simulation of the puzzle is done to find its effectiveness.

The code "MCTS.py" can be run after making changes in the input csv file. 