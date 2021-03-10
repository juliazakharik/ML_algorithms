"""
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

"""

class Solution(object):
    #Runtime: 564 ms, faster than 95.28%
    #Memory Usage: 23.2 MB, less than 66.71%
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        total = 0
        for num in d:
            if k - num == num:
                total += (d[num] // 2)
                d[num] = 0
            elif d[num] == 0:
                continue
            elif k - num in d:
                total += min(d[num], d[k-num])
                d[num] = 0
                d[k-num] = 0
        return total