# Create a function named circus_parade_lineup that receives performers as its parameter.

# This function aims to sort the performers alphabetically by their act names and create a string that announces the parade lineup.

# The performers list contains strings, where each string represents a performer. 
# The string format is "performer_id-act_name", with the performer's unique identifier and their act name separated by a hyphen. 
# For example, "123-Clown Act" represents a performer with ID 123 and the act name "Clown Act".

# To solve this challenge, follow these steps:

# Extract the act names from the performers list.
# Sort the act names alphabetically.
# Create a new list to store the performer IDs in the order of their sorted act names.
# Join the sorted performer IDs into a single string, separated by commas.
# Return the resulting string that announces the parade lineup.
# Parameters:

# performers (list): A list of strings, where each string represents a performer in the format "performer_id-act_name".
# The function returns a string that lists the performers' identifiers in the order of their sorted act names, separated by commas.


def circus_parade_lineup(performers):
    # Write code here 
    my_dict = {}
    for i in performers:
        findHypen = i.find('-')
        my_dict[i[:findHypen]] = i[findHypen + 1:]

    cc = sorted(my_dict.items(), key=lambda x:x[1])
    res = []

    for val, y in cc:
        res.append(val)
    return ', '.join(res)

print(circus_parade_lineup(['1-Zebra Taming', '2-Yodeling', '3-Xylophone Playing']))