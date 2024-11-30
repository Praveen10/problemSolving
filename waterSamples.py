# Create a function named analyze_water_samples that receives samples as its parameter.

# This function aims to analyze the pH levels of various water samples collected by a scientist. 
# The scientist wants to determine the range of acidity or basicity across the samples.

# To achieve this, sort the samples array in ascending order. This will arrange the pH levels from the most acidic to the most basic. 
# Then, calculate the difference between the highest and lowest pH levels to find the range.

# Additionally, keep track of the number of samples that have a neutral pH level of exactly 7.0. 
# Increment a counter for each neutral sample encountered.

# Parameters:

# samples (float-array): An array of float numbers representing the pH levels of water samples. 
# Each pH level ranges between 0 and 14, where 7 is considered neutral, values below 7 are acidic, and values above 7 are basic.
# The function returns a float value representing the range of pH levels, 
# which is the difference between the highest and lowest pH values in the sorted samples array.


def analyze_water_samples(samples):
    samples.sort()
    pHRange = float(samples[-1] - samples[0])

    neturalCount = 0
    for i in samples:
        if i == 7.0:
            neturalCount += 1
    
    return pHRange

print(analyze_water_samples([7, 7, 7]))