# Create a function named junkyard_palindrome that receives items as its parameter.

# This function aims to determine if the reversed names of the given junkyard items can be rearranged to form a palindrome.

# In this challenge, you will help an old robot named Rusty to check if the reversed names of the items from the 
# junkyard can be rearranged to create a palindrome. To solve this problem, follow these steps:

    # 1.Reverse the name of each item in the items list.
    # 2.Check if the reversed names can be rearranged to form a palindrome.
    # 3.Use break and continue statements efficiently to skip unnecessary checks and flag possible palindrome formations early.
    # 4.Ensure the function considers optimal stopping conditions using advanced break and continue 
    #   logic to make the solution efficient even for the maximum input sizes.

def junkyardPalindrome(items):
    charCount = {}
    for item in items:
        reversedItem = item[::-1]
        for char in reversedItem:
            if char.isalpha():  
                char = char.lower()  
                charCount[char] = charCount.get(char, 0) + 1
    oddCount = 0
    for count in charCount.values():
        if count % 2 != 0:
            oddCount += 1
            if oddCount > 1:
                return "No"  
    
    return "Yes"

print(junkyardPalindrome(["racecar, level, world, hello"]))