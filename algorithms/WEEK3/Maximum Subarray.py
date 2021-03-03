"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i, len(nums) - 1): 
                if max_sum < s:
                    max_sum = s
                s += nums[j + 1]
            if max_sum < s:
                    max_sum = s
        return max_sum