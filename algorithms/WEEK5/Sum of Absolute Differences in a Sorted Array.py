"""
1685. Sum of Absolute Differences in a Sorted Array
Share
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.


Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
"""


class Solution(object):
    #Runtime: 832 ms, faster than 91.22%
    #Memory Usage: 28 MB, less than 93.92%

    #Runtime: 812 ms, faster than 97.97%
    #Memory Usage: 28.1 MB, less than 87.84%
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sum_ = sum(nums)
        l = len(nums)
        for i in range(l):
            res.append(sum_ + nums[i] * (2 * i - l))
            sum_ -= 2 * nums[i]
        return res