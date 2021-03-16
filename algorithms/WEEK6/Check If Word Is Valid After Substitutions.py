"""
1003. Check If Word Is Valid After Substitutions

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
"""


#Runtime: 180 ms, faster than 25.42% of Python online submissions for Check If Word Is Valid After Substitutions.
# Memory Usage: 13.5 MB, less than 94.92% of Python online submissions for Check If Word Is Valid After Substitutions.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s != "":
            ind = s.find('abc')
            s = s[:ind] + s[ind + 3:]
            if ind == -1:
                return False
        return True


# Runtime: 20 ms, faster than 95.76% of Python online submissions for Check If Word Is Valid After Substitutions.
# Memory Usage: 13.4 MB, less than 99.15% of Python online submissions for Check If Word Is Valid After Substitutions.class Solution(object):
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """   
    while s != "":
        prev_len = len(s)
        s = s.replace('abc', '')
        if len(s) == prev_len:
            return False
    return True
            