# Create a function named reverse_microscopic_segment that receives sequence and indices as its parameters.

# This function aims to reverse a specific segment of a microscopic sequence based on the provided indices.

# A scientist is studying a microscopic sequence under a powerful microscope. 
# To better understand a particular segment of the sequence, they need to reverse the 
# order of elements within a specific range.

# The function should use the first two integers in the indices list to 
# determine the start and end of the slicing operation on the sequence. 
# After extracting the substring, the function should return the reversed version of this substring.

# Parameters:
# sequence (str): The microscopic sequence represented as a string.
# indices (list): A list of two integers representing the start and end indices of the segment to be reversed.
# The function returns a string representing the modified sequence with the specified segment reversed.

def reverseMicroscopicSegment(sequence, indices):
    # Write code here 
    start, end = indices
    segment = sequence[start:end]
    reversedSegment = segment[::-1]
    return sequence[:start] + reversedSegment + sequence[end:]

print(reverseMicroscopicSegment('PYTHON', [0, 6]))