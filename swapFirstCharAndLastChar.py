# Create a function named swap_characters that receives input_string as its parameter.

# This function aims to create a new string by swapping the first and last characters of the given input_string.

# To achieve this, follow these steps:

# Check if the length of the input_string is less than 2. If so, return the input_string as is since swapping is not possible.
# Store the first character of the input_string in a variable.
# Replace the first character of the input_string with the last character.
# Replace the last character of the input_string with the stored first character.
# Return the modified input_string.
# Parameter:

# input_string (str): The input string that needs to have its first and last characters swapped.
# The function should return a string with the first and last characters of the input_string swapped.


def swapCharacters(input_string):
    if not input_string:
        return ''
    inputLength = len(input_string)
    if inputLength < 2:
        return input_string
    else:
        return input_string[-1] + input_string[1 : -1] + input_string[0]
    
print(swapCharacters('hello'))