# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

 

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Answer

def longestCommonPrefix(strs):
    if not strs:
        return "" 

    strs.sort()

    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break
    
    return prefix   


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))