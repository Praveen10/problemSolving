# Find the Longest Palindromic Substring

# A palindromic substring is a substring of a given string that reads the same forwards and backwards.

# Write a function longest_palindromic_substring(s) that takes a string s as input and returns the longest palindromic substring.

def longestPalindromicSubstring(a1):
    if not a1:
        return ''
    longest = ''
    for i in range(len(a1)):
        for j in range(i, len(a1)):
            subStr = a1[i:j+1]
            if subStr == subStr[::-1]: 
                if len(subStr) > len(longest):  
                    longest = subStr
    return longest

print(longestPalindromicSubstring('babad'))