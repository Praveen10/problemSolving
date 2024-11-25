# Create a function named glowingFlowers that receives flowerColors and currentHour as its parameters.

# This function aims to determine which flowers in a secret garden glow at a specific hour based on their color codes.

# Imagine a secret garden at dusk, where each flower has a unique color code represented as a binary string (e.g., "1010").
# To determine if a flower glows, you need to convert its binary color code to a decimal number and add the current hour to it. If the resulting sum is an odd number, the flower glows; otherwise, it remains dim.

# Your task is to create a function that takes an array of flower color codes and the current hour, 
# and returns a new array containing only the color codes of the glowing flowers.

# Parameters:

# flowerColors (string-array): An array of binary strings, where each string represents a flower's color code.
# currentHour (integer): The current hour, an integer value between 0 and 23 (inclusive).
# The function returns a string-array, which is a new array containing the color codes of the glowing flowers.

def glowingFlowers(flowerColors, currentHour):
    res = []
    for i in flowerColors:
        convert = int(i, 2)
        if (convert + currentHour) % 2 == 1:
            res.append(i) 
    return res


print(glowingFlowers(['1111', '0000', '1010', '0101'], 12))