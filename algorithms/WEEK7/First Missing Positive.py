"""
41. First Missing Positive
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2

"""

# Runtime: 20 ms, faster than 84.62% of Python online submissions for First Missing Positive.
# Memory Usage: 13.4 MB, less than 66.69% of Python online submissions for First Missing Positive.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) + 2
        nums = set(nums)
        for i in range(1, l):
            if i not in nums:
                return i
        return 1