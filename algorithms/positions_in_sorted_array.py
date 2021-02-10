"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        min_ = 0
        max_ = len(nums) - 1
        min_ind = -1
        max_ind = -1
        prev_med = -1
        if(len(nums) == 0):
            return [min_ind, max_ind]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1, -1]
        while True:
            med = (max_ + min_) // 2
            if prev_med == med:
                break
            elif nums[med] < target:
                 min_= med
            elif nums[med] > target:
                max_ = med
            else:
                i = med
                max_ind = i
                while True:
                    if i + 1 < len(nums) and nums[i+1] == target:
                        max_ind = i+1
                    else:
                        break;
                    i += 1
                i = med
                min_ind = i
                while True:
                    if i - 1 < len(nums) and i - 1 >= 0 and nums[i-1] == target:
                        min_ind = i-1
                    else:
                        break;
                    i -= 1
                break
            prev_med = med
        return [min_ind, max_ind]