# Create a function named flashing_lights that receives lights as its parameter.

# This function aims to simulate a flashing light pattern for a festive event. 
# The lights are arranged in a linear array, and each light is represented by an integer value of either 0 (off) or 1 (on).

# The flashing pattern follows these rules:

# Every third light (index 2, 5, 8, etc.) toggles its state. If it's on (1), it becomes off (0), and if it's off (0), it becomes on (1).
# The first and last lights in the array always remain in their initial state and are not affected by the flashing pattern.
# Your task is to implement the flashing_lights function that takes the initial 
# state of the lights as input and returns a new array representing the state of the lights after one cycle of the flashing pattern.

# Parameters:

# lights (list): A list of integers where each integer is either 0 (off) or 1 (on), representing the initial state of the lights.
# The function returns a new list of integers representing the state of the lights after one cycle of the flashing pattern.

def flashing_lights(lights):
    temp = 2
    res = []
    for i in range(len(lights)):
        if (i + 1) == len(lights):
            res.append(lights[i])
        elif i == temp:
            if lights[i] == 0:
                res.append(1)
            else:
                res.append(0)
            temp += 3
        else:
            res.append(lights[i])
    return res

print(flashing_lights([0, 1, 0, 1, 0, 1, 0]))