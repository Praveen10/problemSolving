# def twoSum(nums, target):
#     countNumber = 0
#     arrPlace = []
#     for index, value in enumerate(nums):
#         addTwoNumber = countNumber + value
#         countNumber = value
#         if len(arrPlace) > 1:
#             arrPlace[0] = arrPlace[1]
#             arrPlace[1] = index
#         else:
#             arrPlace.append(index)
#         if addTwoNumber == target:
#             return arrPlace


# twoSum([2,7,11,15], 9)



# The Solution

def twoSum(nums, target):
    index_map = {}  
    for index, value in enumerate(nums):
        complement = target - value
        if complement in index_map:
            return [index_map[complement], index]
        index_map[value] = index
    return []

result = twoSum([2,7,11,15], 9)
print(result)