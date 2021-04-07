"""
747. Largest Number At Least Twice of Others
Easy

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

"""

# Runtime: 20 ms, faster than 84.69% of Python online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 13.2 MB, less than 92.18% of Python online submissions for Largest Number At Least Twice of Others.
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        m_i = 0
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                m_i = i
        m /= 2     
        for i in range(len(nums)):
            if nums[i] > m and m_i != i:
                return -1
        return m_i
        