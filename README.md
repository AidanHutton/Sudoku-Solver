# Sudoku-Solver
Playable sudoku game that can be solved with the click of a button!
Press the space key to watch the game solve itself!


This program will utilize recurrsion in the way of backtracking to solve any given sudoku board. 
We start the program by initializing the sudoku board in the form of a matrix, or 2d array, and set all the values to 0. We will replace these values later in the 
program to make the game playable and make sure that there is always a valid solution. Once this is created, we will make a function to linearly search through the
matrix and return the first 0 that it can find. A 0 value means that this is a number that needs to be solved and a square that needs to be tested in order to solve
the puzzle. Once we return the index of this 0 value we can then move onto testing the number to see if it is valid by the rules of sudoku. We will check to see if the
number is located in the same row, column and 3x3 box and if it is found we know that the number is not valid. We will put both of these functions into a solve 
function to search for the 0 values, test what numbers fit within that index and once the computer can no longer find a value that works it will backtrack to the last 
number that did work and retest the numbers until there are no 0's left. 

Along with this we will have other functions to generate a new board so that every time you play it is different as well as a function to remove numbers in order to
make the game playable. To generate the board we will use the solve board function but instead of testing values 1-9 it will add a random number 1-9 to make sure the
board is always random. The remove number function will simply go and delete random number from the board so that you can insert your own values and play the game. 

The rest of this program is the GUI, the first one I have ever made, and allows the user to select a square and have it highlighted so that you can insert a value 1-9. 
You can also press the ESC key to delete any values that you no longer want on the board. Once you no longer want to play, simply press the spacebar and sit back while 
the computer does the work for you!
