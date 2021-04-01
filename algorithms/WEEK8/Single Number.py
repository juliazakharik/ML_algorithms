"""
136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1

"""

# Runtime: 112 ms, faster than 62.99% of Python online submissions for Single Number.
# Memory Usage: 16.1 MB, less than 41.85% of Python online submissions for Single Number.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key in d.keys():
            if d[key] == 1:
                return key



# Runtime: 112 ms, faster than 62.99% of Python online submissions for Single Number.
# Memory Usage: 15.7 MB, less than 59.27% of Python online submissions for Single Number.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]