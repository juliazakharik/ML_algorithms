"""
260. Single Number III
Medium

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

"""

# Runtime: 32 ms, faster than 98.85% of Python online submissions for Single Number III.
# Memory Usage: 15.7 MB, less than 22.99% of Python online submissions for Single Number III.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        res = []
        for key in d.keys():
            if d[key] == 1:
                res.append(key)
            if len(res) == 2:
                return res


# Runtime: 40 ms, faster than 89.66% of Python online submissions for Single Number III.
# Memory Usage: 15.6 MB, less than 37.16% of Python online submissions for Single Number III.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums:
            if d[num] == 1:
                del d[num]
            else:
                d[num] += 1
        return d.keys()