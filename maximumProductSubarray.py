# Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


def maxProductSubarray(nums):
    if not nums:
        return 0

    currentMax = currentMin = maxProduct = nums[0]

    for num in nums[1:]:
        if num < 0:
            currentMax, currentMin = currentMin, currentMax

        currentMax = max(num, currentMax * num)
        currentMin = min(num, currentMin * num)

        maxProduct = max(maxProduct, currentMax)

    return maxProduct

nums = [2, 3, -2, 4]
result = maxProductSubarray(nums)
print(result) 