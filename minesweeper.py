import random

# global variable to set the width and length of the square grid


GRID_SIZE = 8


######################################################
# this function places mines randomly in the minefield
######################################################

def placeMines():
    
    '''
    Places mines randomly (probablity of 1/10) across the board.

            Parameters:
                    none 

            Returns:
                    grid containing mines (minefield)
    '''
    
    # 1/10 chance of finding a mine in each coordinate
    options = ["X", "0"]
    weights = [0.1, 0.9]
    # returns a 2D list representing the
    # minefield: 0 for empty, and X for a mine
    return [
        [random.choices(options, weights)[0] for i in range(GRID_SIZE)]
        for j in range(GRID_SIZE)
    ]


######################################################
# this function makes a game board (cells are hidden)
# cells are hidden using '#'
######################################################

def makeBoard():
    
    '''
    This function makes the gameboard (hidden cells represented by '#').

            Parameters:
                    none 

            Returns:
                    grid with hidden cells (gameboard, ie, what player sees)
    '''
    
    return [['#'] * GRID_SIZE for i in range(GRID_SIZE)]


######################################################
# this function takes a 2D list and 
# displays the board to the user
######################################################

def showBoard(myGameboard):
    
    '''
    Prints the gameboard.

            Parameters:
                    gameboard (2D List) 

            Returns:
                    none
    '''
    
    print("\n")
    print(" |", end = "")
    for i in range(GRID_SIZE):
        print(str(i), end = " ")
        
    print("\n" + " - "*(GRID_SIZE), end = "")
    
    for i in range(GRID_SIZE):
        print()
        print(i,end="|")
        
        for j in range(GRID_SIZE):
            print(myGameboard[i][j], end=" ")
    
    print()


######################################################
# this function takes a 2D list and
# counts the number of hidden cells
# initially this is all the cells
    #this numer reduces as the game progresses
######################################################

def countHiddenCells(myGameboard):
    
    '''
    Function counts the number of hidden cells in the board (count).
    Initially, this is all the cells.
    The number reduces with every pass.

            Parameters:
                    gameboard (2D List) 

            Returns:
                    count (int)
    '''
    
    return sum(sum(col == '#' for col in row) for row in myGameboard)


######################################################
# this function takes a 2D
# list and counts the number of mines
######################################################

def countAllMines(myMinefield):
    
    '''
    Counts the number of mines (count).

            Parameters:
                    myMinefield (2D List) 

            Returns:
                    count (int)
    '''
    
    return sum(sum(col == 'X' for col in row) for row in myMinefield)


######################################################
# this functions takes a 2D list, a row,
# and a column and determines
# whether a mine is in that location
######################################################
    
def isMineAt(myMinefield, row, column):
    
    '''
    Checks if the location has a mine or not.
    It also checks if the location is a valid one.

            Parameters:
                     myMinefield (2D List), row (int), col (int)

            Returns:
                    True/ False (boolean)
    '''
    
    if 0 <= row < GRID_SIZE and 0 <= column < GRID_SIZE:
        return myMinefield[row][column] == "X"
    return False


######################################################
# this function takes a 2D list, a row, and a column
# it counts the number of adjacent mines
######################################################
        
def countAdjacentMines(myMinefield, row, column):
    
    '''
    Counts the number of mines in the adjacent 8 locations of the current cell.

            Parameters:
                    myMinefield (2D List), row (int), col (int)

            Returns:
                    count
    '''
    
    count = 0
    # (row-1, col-1)
    if row >= 1 and column >= 1:
        if myMinefield[row-1][column-1] == "X":
            count += 1
    # (row-1, col)
    if row >= 1:
        if myMinefield[row - 1][column] == "X":
            count += 1
    # (row-1, col+1)
    if row >= 1 and column + 1 < GRID_SIZE:
        if myMinefield[row - 1][column + 1] == "X":
            count += 1
    # (row, col-1)
    if column - 1 >= 0:
        if myMinefield[row][column - 1] == "X":
            count += 1
    # (row, col+1)
    if column + 1 < GRID_SIZE:
        if myMinefield[row][column + 1] == "X":
            count += 1
    # (row+1, col-1)
    if row + 1 < GRID_SIZE and column >= 1:
        if myMinefield[row + 1][column - 1] == "X":
            count += 1
    # (row+1, col)
    if row + 1 < GRID_SIZE:
        # print("row+1:", row+1, "column:", column)
        if myMinefield[row + 1][column] == "X":
            count += 1
    # (row+1, col+1)
    if row+1 < GRID_SIZE and column+1 < GRID_SIZE:
        if myMinefield[row+1][column+1] == "X":
            count += 1
    return count


######################################################
# this functions takes a row
# and column checks for a valid input
######################################################
    
def isValid(row, column):
    
    '''
    Checks whether location is valid.

            Parameters:
                    row (int), col (int) 

            Returns:
                    True/ False (boolean)
    '''
    
    return (0 <= row < GRID_SIZE) and (0 <= column < GRID_SIZE)


######################################################
# this function takes two 2D lists, a row and a column
# It reveals the updated board
# does no return a value
# work is done in mutating the board
######################################################
        
def reveal(myGameboard, myMinefield, row, col):
    
    '''
    Recursive function.
    Reveals the updated gameboard.

            Parameters:
                    myGameboard (2D List), myinefield (2D List), row (int), col (int)

            Returns:
                    none
    '''
    
    numAdjacentMines = countAdjacentMines(myMinefield, row, col)
    
    if not (0 <= row < GRID_SIZE) or not (0 <= col < GRID_SIZE):
        return
    
    if isMineAt(myMinefield, row, col):
        myGameboard[row][col] = "X"
        
        for i, myRow in enumerate(myMinefield):
            
            for j, element in enumerate(myRow):
                if isMineAt(myMinefield, i, j):
                    myGameboard[i][j] = "X"
        return
    
    elif myGameboard[row][col] == " ":
        return
    
    else:
        if numAdjacentMines == 0:
            myGameboard[row][col] = " "
            pairs = [
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1),
                (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
            ]
            for item in pairs:
                if isValid(*item) and not isMineAt(myMinefield, *item):
                    reveal(myGameboard, myMinefield, *item)
        
        else:
            myGameboard[row][col] = numAdjacentMines
            return
            # return myGameboard

######################################################
# function checks whether the user input is valid
######################################################

def isValidInput(myStr):
    
    '''
    Checks whether the user's input is valid or not.

            Parameters:
                    myStr (user input) (string)

            Returns:
                    True/ False (boolean)
    '''
    
    first = second = -1
    
    if __import__('re').match('^[0-9],[0-9]$', myStr):
        first, comma, second = myStr
    
    if (0 <= int(first) < GRID_SIZE) and (0 <= int(second) < GRID_SIZE):
        return True
    
    print("\nPlease enter a valid input")
    return False

######################################################
# main function
        # first, checks user input
        # second, if no. of hiden cells = no. of mines
            # game is terminated
######################################################
        
def main():
    
    '''
    Main function.

            Parameters:
                    none 

            Returns:
                    none
    '''
    
    move = ""
    minefield = placeMines()
    gameboard = makeBoard()
    print("\n\n\nMINESWEEPER\n------------\n")
    showBoard(minefield)
    showBoard(gameboard)
    while True:
        # get user's move
        while True:
            move = input("\nSelect a cell (row,col): > ")
            if isValidInput(move):
                break
        row = int(move[0])
        col = int(move[2])
        reveal(gameboard, minefield, row, col)
        if countAllMines(minefield) == countAllMines(gameboard):
            showBoard(gameboard)
            print("\nGame over! You lost!")
            break
        if countHiddenCells(gameboard) == countAllMines(minefield):
            showBoard(gameboard)
            print("\nGame over! You win!")
            break
        showBoard(gameboard)


main()
