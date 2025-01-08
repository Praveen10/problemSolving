# Create a function named admire_garden_sections that receives garden, start, and end as its parameters.

# This function aims to extract specific sections of plants from each row of a garden, represented as a list of lists, 
# and return these sections as a new list of lists.

# Imagine you're in a beautiful backyard garden, filled with rows of flowering plants. Each plant in a row is of a different type,
#  represented by a unique string. You want to admire specific sections of these plants.

# The garden parameter is a list of lists, where each inner list represents a row of plants. The start and end parameters are integers 
# representing the starting and ending positions (inclusive) of the plant sections you want to admire.

# Your task is to create a new list of lists containing only the plants within the specified start and end positions from each row. 
# Remember, you're admiring sections, so the start and end positions apply to each row independently.

# For example, given the following garden:

# [
#     ["rose", "tulip", "daisy", "lily", "orchid"],
#     ["sunflower", "jasmine", "iris", "lavender", "peony"],
#     ["marigold", "daffodil", "poppy", "chrysanthemum", "dahlia"]
# ]
# If start = 1 and end = 3, the expected output would be:

# [
#     ["tulip", "daisy"],
#     ["jasmine", "iris"],
#     ["daffodil", "poppy"]
# ]
# Note:

# The start and end positions are 0-indexed.
# The start position will always be less than or equal to the end position.
# The end position will always be less than the length of each inner list.
# Parameters:

# garden (list of lists of strings): A list of lists representing the rows of plants in the garden. 
# Each inner list contains strings representing the types of plants in that row.
# start (int): An integer representing the starting position (inclusive) of the plant sections to admire.
# end (int): An integer representing the ending position (inclusive) of the plant sections to admire.
# The function should return a new list of lists containing the admired plant sections from each row of the garden.


def admire_garden_sections(garden, start, end):
    # Write code here 
    return [row[start:end] for row in garden]

print(admire_garden_sections([["rose", "tulip", "daisy", "lily", "orchid"], ["sunflower", "jasmine", "iris", "lavender", "peony"], ["marigold", "daffodil", "poppy", "chrysanthemum", "dahlia"]], 1, 3)) # [["tulip", "daisy"], ["jasmine", "iris"], ["daffodil", "poppy"]]