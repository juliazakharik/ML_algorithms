"""
326. Power of Three
Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true

"""

# Runtime: 60 ms, faster than 87.57% of Python online submissions for Power of Three.
# Memory Usage: 13.4 MB, less than 67.76% of Python online submissions for Power of Three.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1: return True
        two = 3
        while True:
            if n > two:
                two *= 3
            elif n == two:
                return True
            else: return False