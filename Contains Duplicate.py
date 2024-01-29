# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Answer

def containsDuplicate(nums):
    uniqueElements = set()

    for number in nums:
        if number in uniqueElements:
            return True

        uniqueElements.add(number)
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
containsDuplicate(nums)