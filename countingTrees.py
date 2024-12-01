# Create a function named count_trees_on_trail that receives steps_taken as its parameter.

# This function aims to count the number of trees encountered on a hiking trail based on the binary representation
# of the number of steps taken. The trail is marked with a sequence of '1's (representing a tree) and '0's (representing no tree)
# that follows a binary counting pattern.

# To solve this challenge, you need to:

# Convert the steps_taken to its binary string representation.
# Count the number of '1's in the binary string, as each '1' represents a tree encountered on the trail.
# Return the total count of trees encountered.
# Parameters:

# steps_taken (int): The number of steps taken on the trail. It will be a non-negative integer.
# The function returns an integer representing the total number of trees encountered on the trail within the given number of steps.

def countTreesOnTrail(steps_taken):
    binarySteps = bin(steps_taken)[2:]
    return binarySteps.count('1')

print(countTreesOnTrail(7))