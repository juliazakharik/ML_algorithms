"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

 Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
    #Runtime: 24 ms, faster than 58.36%
    #Memory Usage: 13.4 MB, less than 42.15%
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            sum_ = 0
            while n != 0:
                sum_ += (n % 10) ** 2
                n //= 10
            if sum_ == 1:
                return True
            if sum_ in seen:
                return False
            seen.add(sum_)
            n = sum_


        #Runtime: 16 ms, faster than 94.64%
        #Memory Usage: 13.7 MB, less than 14.76%
        def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while True:
            sum_ = 0
            while n != 0:
                sum_ += (n % 10) ** 2
                n //= 10
            if sum_ == 1:
                return True
            if sum_ in seen:
                return False
            seen.append(sum_)
            n = sum_