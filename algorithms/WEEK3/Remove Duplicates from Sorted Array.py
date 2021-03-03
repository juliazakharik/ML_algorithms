"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: it
        """
        if len(nums) == 0: return 0
        prev = nums[0]
        l = 1
        new_ind = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[new_ind] = nums[i]
                new_ind += 1
                l += 1
            prev = nums[i]
        print(l, nums)
        return l