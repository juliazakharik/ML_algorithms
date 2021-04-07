"""
342. Power of Four
Easy
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false

"""

# Runtime: 16 ms, faster than 78.29% of Python online submissions for Power of Four.
# Memory Usage: 13.4 MB, less than 66.28% of Python online submissions for Power of Four.
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1: return True
        two = 4
        while True:
            if n > two:
                two *= 4
            elif n == two:
                return True
            else: return False