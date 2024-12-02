# Create a function named create_flower_tags that receives flower_names and separator as its parameters.

# This function aims to help Jenny format her list of flower names into individual tags for each flower pot in her grandmother's garden.

# The flower_names parameter is a string containing multiple flower names concatenated together, with each name separated by the separator string.

# Your task is to split the flower_names string into individual flower names using the provided separator, 
# then wrap each flower name with the <tag> and </tag> tags.

# The resulting tagged flower names should be combined into a single string, with each tagged name separated by a newline character (\n).

# Parameters:

# flower_names (str): A string containing flower names concatenated together, separated by the separator string.
# separator (str): The string used to separate individual flower names within the flower_names string.
# The function should return a string with each flower name wrapped in <tag> and </tag> tags, 
# and each tagged name separated by a newline character.

def create_flower_tags(flower_names, separator):
    flowers = flower_names.split(separator)
    res = []
    for i in flowers:
        res.append(f"<tag>{i}</tag>")
    return "\n".join(res)
        
print(create_flower_tags('Daisy;Sunflower;Tulip', ';'))