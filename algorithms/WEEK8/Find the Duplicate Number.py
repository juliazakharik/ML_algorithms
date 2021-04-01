"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

# Runtime: 48 ms, faster than 79.79% of Python online submissions for Find the Duplicate Number.
# Memory Usage: 15 MB, less than 99.77% of Python online submissions for Find the Duplicate Number.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            nums[abs(num) - 1] *= (-1)

# Runtime: 52 ms, faster than 61.60% of Python online submissions for Find the Duplicate Number.
# Memory Usage: 15.3 MB, less than 59.68% of Python online submissions for Find the Duplicate Number.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1



