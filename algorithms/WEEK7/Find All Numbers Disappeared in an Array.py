"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""
# Runtime: 288 ms, faster than 96.46% of Python online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 23.3 MB, less than 32.13% of Python online submissions for Find All Numbers Disappeared in an Array.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums) + 1
        nums = set(nums)
        res = []
        for i in range(1, l):
            if i not in nums:
                res.append(i)
        return res
    