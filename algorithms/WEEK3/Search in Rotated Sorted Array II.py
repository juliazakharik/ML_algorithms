"""
81. Search in Rotated Sorted Array II
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        rotated_ind = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rotated_ind = i
        if target < nums[0]:
            start = rotated_ind
            end = len(nums) - 1
        else:
            start = 0
            end = rotated_ind - 1

        
        found = -1
        while start <= end:
            mid = start + (end - start) // 2
            print(nums, mid, start, end)
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        return -1