"""
231. Power of Two
Easy

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
"""
#2 solutions
        
# Runtime: 12 ms, faster than 97.04% of Python online submissions for Power of Two.
# Memory Usage: 13.4 MB, less than 39.26% of Python online submissions for Power of Two.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1: return True
        two = 2
        while True:
            if n > two:
                two *= 2
            elif n == two:
                return True
            else: return False

# Runtime: 16 ms, faster than 83.15% of Python online submissions for Power of Two.
# Memory Usage: 13.5 MB, less than 11.11% of Python online submissions for Power of Two.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else: return False
        return True