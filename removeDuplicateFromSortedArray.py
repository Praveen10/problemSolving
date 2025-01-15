# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
# each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were 
# present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }


def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        temp = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[temp]:
                temp += 1
                nums[temp] = nums[i]
        return temp + 1

print(removeDuplicates([1,1,2])) # 2