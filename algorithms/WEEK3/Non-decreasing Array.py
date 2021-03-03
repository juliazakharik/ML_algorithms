"""
665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] and flag:
                print(i, ' ', nums[i-1], ' ', nums[i+1])
                if i == 0 or i >= (len(nums) - 2) or nums[i - 1] <= nums[i + 1] or nums[i] <= nums[i + 2]:
                    flag = False
                else:
                    return False
            elif nums[i] > nums[i + 1] and not flag:
                return False
        return True