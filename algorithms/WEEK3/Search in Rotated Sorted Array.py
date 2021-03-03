"""
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

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