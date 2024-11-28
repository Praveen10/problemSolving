# Create a function named garden_planner that receives flowers and fruits as its parameters.

# This function aims to help plan the arrangement of a backyard garden by combining and rearranging lists of flowers and fruits to be planted.

# The function should first concatenate the flowers and fruits arrays together into a single array.
# Then, it should reverse the order of the elements in the combined array, as if rearranging the planting plan.

# Finally, the function should return the modified array that represents the final planned arrangement of flowers and fruits in the garden.

# Parameters:

# flowers (list): A list of strings, where each string is the name of a type of flower to be planted in the garden.
# fruits (list): A list of strings, where each string is the name of a type of fruit to be planted in the garden.
# The function returns a list of strings representing the final arrangement of flowers and fruits in the garden, 
# with the elements of fruits first (in reverse order) followed by the elements of flowers (also in reverse order).

def gardenPlanner(flowers, fruits):
    res = []
    def storeValue(item):
        if not item:
            res.append('')
            
        for i in item[::-1]:
            res.append(i)
            
    storeValue(flowers)
    storeValue(fruits)
    return res

print(gardenPlanner(['sunflower', 'daisy', 'tulip', 'rose'], ['orange', 'banana', 'pear', 'apple']))