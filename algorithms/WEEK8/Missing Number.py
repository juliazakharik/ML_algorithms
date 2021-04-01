"""
268. Missing Number
Easy
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

"""
# Runtime: 116 ms, faster than 42.95% of Python online submissions for Missing Number.
# Memory Usage: 14.6 MB, less than 70.71% of Python online submissions for Missing Number.
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for num in nums:
            if num % (l + 1) != l:
                nums[num % (l + 1)] += l + 1
        for i in range(l):
            if nums[i] <= l:
                return i
            
        return l