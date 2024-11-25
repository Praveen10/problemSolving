# Create a function named spicewood_shade that receives sentence as its parameter.

# This function aims to reverse each word in the given sentence, but it should skip words that contain the letter 'e'.

# Imagine you are relaxing in the shade of a spicewood tree, and you decide to engage in a word game to pass the time. 
# You challenge yourself to reverse each word in a sentence, but with a twist: you will skip any word that contains the letter 'e'.

# To solve this challenge, you can split the sentence into individual words and iterate over each word. 
# For each word, check if it contains the letter 'e'. If it does not, reverse the word; otherwise, leave the word as is. 
# Finally, join the words back together to form the modified sentence.

# Parameters:

# sentence (str): The input sentence containing words separated by spaces. 
# The sentence will contain at least one word and a maximum of 100 words. 
# Each word will consist of lowercase English letters only.
# The function returns a string representing the modified sentence, 
# where each word is reversed if it does not contain the letter 'e', and left unchanged otherwise.


def spicewood_shade(sentence):
    res = []
    words = sentence.split()
    for i in words:
        if i.find("e") == -1:
            i = i[::-1]
        res.append(i)
        
    return ' '.join(res)
        
print(spicewood_shade('a elephant is a big animal'))