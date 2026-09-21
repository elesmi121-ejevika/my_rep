# class Solution2(object):
#     def twoSum2(self, nums, target):
#         i = 0
#         output = []
#         while i < len(nums):
#             if target - nums[i] in nums and (target - nums[i] != nums[i] or nums.count(nums[i]) == 2):
#                 output.append(i)
#             i += 1
#         return output
#
# nums1 = [1, 2, 3, 6, 7, 3]
# target1 = 6
#
#
#
# class Solution(object):
#     def twoSum(self, nums, target):
#         i = 0
#         output = []
#         for index, value in enumerate(nums):
#             if target - value in nums and (target - value != value or nums.count(value) == 2):
#                 output.append(index)
#             i += 1
#         return output
#
# print(Solution().twoSum(nums1, target1))

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i

nums1 = [1, 2, 3, 6, 7, 3]
target1 = 6
print(Solution().twoSum(nums1, target1))