import numpy
# ^ NumPY library

SizeColumn = 6
SizeRow = 7
#^^ Parameters for CreateBoard()

def Create_board():
    board = numpy.zeros((SizeColumn, SizeRow))
    return board
# ^^ Return a new array of type board with paremeters for the field.
#has to np.zeros because .array


def Element_location(board, col, row, element ):
    board[col, row] = element
    # ^^ initiate the board with column and row var equal to the element(pice)

def Check_valid_location(board, col):
    for i in range(SizeRow):
        if board[i][col] == 0:
            return i                        # All potential places where element can be placed
    return board[SizeRow-1][col] == 0       #^^ (SizeRow-1) is the size of element, col is location of column in field,  Checking if the location not already filled


def Print_board(board):
    print(board) #origional code contains flip function
    #Attention alteration #