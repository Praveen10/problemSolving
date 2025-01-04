# Write a program that reads a string from standard input and
# outputs only the alphanumeric characters from the string on output

# Input
# He-ll0,W0rl#d!

# Output
# HellWrld

input_string = input()
output_string = ''.join(char for char in input_string if char.isalpha())
print(output_string)