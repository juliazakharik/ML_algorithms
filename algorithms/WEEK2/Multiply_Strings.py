"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example:
Input: num1 = "123", num2 = "456"
Output: "56088"

"""
class Solution(object):
	"""
	Runtime: 12 ms
    Memory Usage: 13.7 MB
	"""
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

    #Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """
    Runtime: 28 ms
    Memory Usage: 13.4 MB
    """
    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        
        """
        res_num1 = 0
        res_num2 = 0
        for n in num1:
            res_num1 += int(n)
            res_num1 *= 10
        
        for n in num2:
            res_num2 += int(n)
            res_num2 *= 10
        return str((res_num1 / 10) * (res_num2 / 10))