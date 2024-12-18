# John wants to walk 10.000 steps every day, so he could be healthy. But unfortunately, 
# today his pedometer (app for counting steps) doesn't work.

# John already measured that he walked X minutes and ran Y minutes, but he is sure that he still hasn't achieved his 10.000 steps mark.

# Write a program that will calculate how many more steps does John need to make to achieve his goal 
# if you know that when he is walking he makes 2 steps in a second, while when he is running he is making 4 steps in a second.

 

# Write a function named steps that given two natural numbers X and Y from input. 
# Output the remaining steps John needs to make to achieve his goal


def steps(a1, a2):
    steps_from_walking = a1 * 60 * 2  
    
    steps_from_running = a2 * 60 * 4  

    total_steps = steps_from_walking + steps_from_running
    target_steps = 10000

    remaining_steps = target_steps - total_steps

    return max(0, remaining_steps)

print(steps(15, 25))