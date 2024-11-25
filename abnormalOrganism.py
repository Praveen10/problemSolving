# Create a function named simulate_abnormal_growth that receives initial_population, growth_rate, and days as its parameters.

# This function aims to simulate the abnormal growth of a biological organism population over a specified number of days,
# given an initial population size and a daily growth rate.

# The growth of the population each day should be calculated using this formula:

# new_population = current_population + (current_population * growth_rate)
# The growth_rate represents the daily percentage increase in the population, expressed as a decimal.

# For example, if the current_population is 100 and the growth_rate is 0.1, then the new_population for the next day would be 110.

# The function should start with the initial_population and calculate the population for each day,
# for the number of days specified, and store each day's result in an array.

# Finally, the function should return this array, where each element represents the population size at the end of the corresponding day.

# Parameters:

# initial_population (int): The size of the population at the start of the simulation.
# growth_rate (float): The daily population growth rate, expressed as a decimal. For example, a 10% growth rate would be expressed as 0.1.
# days (int): The number of days to simulate the population growth.
# The function returns an array of integers, where each element represents the population size at the end of each day of the simulation.

def simulateAbnormalGrowth(initial_population, growth_rate, days):
    population = [initial_population]
    currentPopulation = initial_population
    
    for _ in range(1, days):
        newPopulation = currentPopulation + (currentPopulation * growth_rate)
        population.append(int(newPopulation))
        currentPopulation = newPopulation
    
    return population
        
print(simulateAbnormalGrowth(100, 0.15, 5))