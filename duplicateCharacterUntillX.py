# Create a function named duplicate_until_x that receives string as its parameter.

# This function aims to duplicate each character in the given string up until the first occurrence of the character 'x'. 
# If 'x' is not present in the string, the function should return the original string unchanged.

# To solve this challenge, you can iterate through each character in the string. For each character, check if it is not 'x'. 
# If it's not 'x', duplicate the character and append it to a new string. If the character is 'x', 
# append it to the new string and then append the remaining characters from the original string (including 'x') 
# to the new string without duplication. Finally, return the new string.

# Parameters:

# string (str): The input string that needs to be processed.
# The function returns a string where each character is duplicated up until the first occurrence of 'x'. 
# If 'x' is not present, the original string is returned unchanged


def duplicateUntilX(string):
    if not string:
        return ''
    res  = []
    strFind = string.find('x')
    if strFind != -1:
        for i in string[:strFind + 1]:
            res.append(i * 2)
        res.append(string[strFind + 1:])
        return ''.join(res)
    else:
        return string
    
print(duplicateUntilX('abcxdef'))