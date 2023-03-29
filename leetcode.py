'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''

# s = [4,4,2,8,9]
# target = 
# for i in range(0,len(s)):
#     print(str(i))
#     print("result is " + str(s[i]) + " and " + str(s[i+1]))

import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1, -1, -1):
            for j in range(0,i):
                if nums[j] + nums[j+n-i] == target:
                    return [j, j+n-i]
        return []