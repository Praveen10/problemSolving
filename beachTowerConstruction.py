# Create a function named beach_tower that receives levels as its parameter.

# This function aims to construct a beach tower representation using asterisks (*), 
# where each level of the tower incrementally increases in width.

# The function should return a list of strings, where each string represents a level of the tower. 
# The levels should be centered and aligned based on the widest level. 
# he top level starts with 1 asterisk, and each subsequent level increases the number of asterisks by 2 (i.e., 1, 3, 5, 7, ...). 
# The width of each level string should accommodate the widest level.

# For example, if the input levels is 3, the expected output would be:

# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]

# In this case, the tower has 3 levels. The first level has 1 asterisk, 
# the second level has 3 asterisks, and the third level has 5 asterisks. 
# Each level string is centered based on the width of the widest level.

# Parameter:

# levels (int): The number of levels the beach tower should have. It represents the height of the tower.
# The function returns a list of strings (string-array), where each string represents a level of the beach tower, 
# centered and aligned based on the widest level.

def beachTower(levels):
    maxWidth = 2 * levels - 1
    tower = []
    
    for i in range(levels):
        numAsterisks = 2 * i + 1
        levelStr = ("*" * numAsterisks).center(maxWidth)
        tower.append(levelStr)
    
    return tower

print(beachTower(3))