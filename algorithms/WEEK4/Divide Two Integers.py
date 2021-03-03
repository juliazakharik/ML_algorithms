"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        mult = 0
        if dividend == divisor:
            return 1
        if dividend == -1 *divisor:
            return -1
            
        i = None
        for i in range(abs(dividend)):
            print(i, " ", mult)
            
            mult += abs(divisor)   
            i += 1
            if mult > abs(dividend):
                break
            
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return i - 1
        elif (dividend > 0 and divisor < 0) or (dividend > 0 and divisor < 0):
            return (i - 1) * (-1)
        elif dividend == 0 and divisor != 0:
            return 0