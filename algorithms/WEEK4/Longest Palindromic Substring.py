"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

"""



class Solution(object):
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        long_pal =""
        isPal = False
        t = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    p = s[i:j + 1]
                    isPal = True
                    for k in range(len(p) // 2 + 1):
                        if p[k] != p[-k - 1]:
                            isPal = False
                            break
                    if isPal and len(p) > len(long_pal):
                        long_pal = p
                        t = j
            i = t
        return long_pal
