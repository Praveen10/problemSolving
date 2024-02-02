# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# My Solution 

# class Solution(object):
#     def productExceptSelf(self, nums):
#         productArray = []
#         for i in nums:
#             a = 1
#             for j in nums:
#                 if j != i:
#                     a = a * j
#             productArray.append(a)
#         return productArray
      

def product_except_self(nums):
    n = len(nums)
    
    # Initialize left and right arrays to store products on the left and right of each element
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(1, n):
        print(i)
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Calculate right products
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product
    
    # Calculate the final result by multiplying left and right products
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

nums1 = [1, 2, 3, 4]
print(product_except_self(nums1))