# Create a function named count_ripe_tomatoes that receives tomatoes as its parameter.

# This function aims to count the number of ripe tomatoes in your backyard garden.

# You are checking your tomato plants in your backyard. Each tomato is represented by a character:

# 'G' for Green (unripe)
# 'Y' for Yellow (almost ripe)
# 'R' for Red (ripe)
# Tomatoes ripen progressively: G -> Y -> R. Due to the sun, tomatoes ripen faster from left to right.

# Given a string tomatoes representing your tomato plants, count how many are red 'R'.

# To solve this challenge, you should:

# Iterate through each character in the tomatoes string.
# Check if the character is 'R' using string comparison.
# If it is 'R', increment a counter variable.
# After checking all characters, return the final count of ripe tomatoes.
# Parameters:

# tomatoes (str): A string representing the tomato plants in your backyard. Each character in the string is either 'G', 'Y', or 'R'.
# The function returns an integer representing the count of ripe tomatoes (represented by 'R') in the tomatoes string.


def count_ripe_tomatoes(tomatoes):
    ripeTomatoes = 0
    for i in tomatoes:
        if i == 'R':
            ripeTomatoes += 1
    return ripeTomatoes

print(count_ripe_tomatoes('RRRRRR'))