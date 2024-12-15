# Create a function named scandaroon_behaviour that receives initial_brashness, actions, and echo_threshold as its parameters.

# This function aims to simulate the brash actions of a scandaroon (a type of pigeon) in an ancient kirk by calculating
# the net effect of its actions based on basic increment, decrement, and logical operations.

# Begin with the initial_brashness level. Iterate over the actions list and modify the brashness level according to the following rules:

# Increase the brashness by 2 for "flap"
# Increase the brashness by 3 for "squawk"
# Decrease the brashness by 1 for "rest"
# Decrease the brashness by 2 for "peck"
# After processing all actions, compare the final brashness level with the echo_threshold. 
# Return True if the final brashness level is greater than or equal to the echo_threshold, otherwise return False.

# Parameters:

# initial_brashness (int): Initial level of brashness of the scandaroon.
# actions (list): A sequence of actions represented as strings. Each action will either increase ("flap", "squawk") or 
# decrease ("rest", "peck") the brashness level.
# echo_threshold (int): The brashness level at which the echo becomes significantly noticeable in the ancient kirk.
# The function returns a boolean value. It returns True if the final brashness level exceeds or meets the echo_threshold, 
# which means the scandaroon's actions create a significant echo. It returns False otherwise.

def scandaroon_behaviour(initial_brashness, actions, echo_threshold):
    brashnessLevel = {
        "flap": 2,
        "squawk": 3,
        "rest": -1,
        "peck": -2
    }
    
    for i in actions:
        if i in brashnessLevel:
            initial_brashness += brashnessLevel[i]

    return initial_brashness >= echo_threshold

print(scandaroon_behaviour(0, [], 0))