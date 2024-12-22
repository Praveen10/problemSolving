# Create a program that reads 2 natural numbers from standard input. Find the average between the two (float), 
# increase the first by that value, and decrease the second by that value. Finally, output the difference between the 2 new numbers

# The two natural numbers are given on standard input, write the program to find their average and do the calculation

# Input
# 11 9

# Output
# Difference is: 22

# Explanation
# The average between 11 and 9 is 10, we increase 11 by 10, and we decrease 9 by then, we get 21 and -1, 
# the difference between the two new numbers is 22

A = int(input())
B = int(input())

C = (A + B) // 2

increaseA = A + C
decreaseB = B - C
print("Difference is:",increaseA - decreaseB)