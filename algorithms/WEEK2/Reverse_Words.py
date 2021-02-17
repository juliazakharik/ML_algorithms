"""
Given an input string s, reverse the order of the words.

Example:

Input: s = "  hello world  "
Output: "world hello"
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        s = filter(lambda x: x != '', s)
        s = s[::-1]
        return " ".join(s)