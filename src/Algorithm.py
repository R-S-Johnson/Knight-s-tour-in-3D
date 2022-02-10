import random

# This knights tour algorithm for 3
# dimensions follows Warnsdorff's Rule:
# from the starting position of the knight
# move to the square where it will have
# the fewest onward moves being sure
# to not visit any cell more than once.

# Applying this rule to 3 dimensions works
# as follows:
# 1) the move of a knight in 3d involves
# moving 1 space in one dimension, 2 spaces
# in a different dimension, and 3 spaces
# in the final dimension (and every
# combination of 1, 2, and 3).
# 2) The knight cannot move outside the
# bounds of the cube shapped "board"
# 3) the board is an 8x8x8 cube

# NOTE: Keep in mind that in 3d, if
# all possible moves can be made,
# the knight must choose between
# 144 different possible moves

# For this specific implementation
# of this algorithm, the steps are
# as follows:

# 1) initialization - to allow the
# movement of the knight to occur
# faster, each cell in the board is
# set up to have it's degree calculated
# beforehand. That is, the number of
# moves a knight could make if
# in that square is stored within
# that square. The knight is also
# placed in a random square on the
# board, returning that starting value

# 2) stepwise motion - A method called
# by our main function allows the knight
# to take the next step, finding an
# available square and moving to it,
# setting that new cell to visited,
# and returning the new position of
# the knight. In the case that the
# knight cannot find a new unvisited
# cell, it will return an error.

# 3) repeat - this stepwise motion is
# repeated size cubed times (unless
# stopped by an error), and the knight
# will have finished!

class KnightsTour():

    def __init__(self, size): # size is changable at the creation of this object, but it should be 8 for testing purposes
        self.__length = size
        self.__width = size
        self.__height = size
        self.__round = 0
        self.__position
        self.__visited
        self.__availableMoves