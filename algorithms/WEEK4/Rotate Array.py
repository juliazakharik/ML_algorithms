"""
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        if len(nums) % 2 == 1:
            av = nums[k]
            for i in range(len(nums) - k): 
                if i + k >= len(nums) - k:
                    tmp = nums[j+1]
                    nums[j] = nums[i+k]
                    nums[i+k] = tmp
                    j += 1
                nums[i + k] = nums[i]
            nums[len(nums)-1] = av
        else:
            for i in range(len(nums) - k):
                if i + k >= len(nums) - k:
                    tmp = nums[j]
                    nums[j] = nums[i+k]
                    nums[i+k] = tmp
                    j += 1
                else:
                    nums[i + k] = nums[i]


    def rotate(self, nums, k):
        nums = nums[k:] + nums[:k]