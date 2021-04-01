"""
137. Single Number II
Medium
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3

"""

# Runtime: 52 ms, faster than 35.38% of Python online submissions for Single Number II.
# Memory Usage: 15.1 MB, less than 55.13% of Python online submissions for Single Number II.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(0, len(nums) - 2, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]





# Runtime: 36 ms, faster than 95.90% of Python online submissions for Single Number II.
# Memory Usage: 15.8 MB, less than 18.46% of Python online submissions for Single Number II.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for key in d.keys():
            if d[key] == 1:
                return key