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
# 48 different possible moves

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
        self.__position = []
        self.__visited = []
        self.__availableMoves = []

    def initialize(self):
        print("Initializing..")
        # set random starting position
        self.__position = [random.randint(0, self.__length-1),
            random.randint(0, self.__length-1),
            random.randint(0, self.__length-1)]
        # initialize visited matrix and set starting position to true
        self.__visited = [[[False for i in range(self.__length)]
            for i in range(self.__length)]
            for i in range(self.__length)]
        self.__beenVisited(self.__position)

        self.__availableMoves = [[[48 for i in range(self.__height)] 
            for j in range(self.__height)]
            for k in range(self.__height)]

        self.__initializeAvailableMoves()

        print("Finished initializing")

        return self.__position



    def __beenVisited(self, position):
        self.__visited[position[0]][position[1]][position[2]] = True

    def __initializeAvailableMoves(self):
        for i in range(self.__length):
            for j in range(self.__width):
                for k in range(self.__height): # for each cell in the board
                    position = [i, j, k]
                    for move in self.__permutation([1, 2, 3]):
                        if self.__isOutside(position, move):
                            self.__availableMoves[i][j][k] -= 1




    def __isOutside(self, position, move):
        if position[0] + move[0] >= self.__height or position[0] + move[0] < 0:
            return True
        if position[1] + move[1] >= self.__height or position[1] + move[1] < 0:
            return True
        if position[2] + move[2] >= self.__height or position[2] + move[2] < 0:
            return True
        return False



    # Formula taken and modified from
    # Geeks for Geeks
    def __permutation(self, lst):
    
        # If lst is empty then there are no permutations
        if len(lst) == 0:
            return []
    
        # If there is only one element in lst then, only
        # one permutation is possible
        if len(lst) == 1:
            return [lst, [lst[0]*-1]]
    
        # Find the permutations for lst if there are
        # more than 1 characters
    
        l = [] # empty list that will store current permutation
    
        # Iterate the input(lst) and calculate the permutation
        for i in range(len(lst)):
            m = lst[i]
        
            # Extract lst[i] or m from the list.  remLst is
            # remaining list
            remLst = lst[:i] + lst[i+1:]
        
            # Generating all permutations where m is first
            # element
            for p in self.__permutation(remLst):
                l.append([m] + p)
                l.append([-1*m] + p)
        return l


if __name__ == "__main__":
#    test = KnightsTour(8)
#    output = test.permutation([1, 2, 3])
#    print(len(output))
#    print(output)
    pass