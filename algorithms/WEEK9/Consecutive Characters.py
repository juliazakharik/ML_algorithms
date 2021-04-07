"""
1446. Consecutive Characters
Easy
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
"""

# Runtime: 28 ms, faster than 79.14% of Python online submissions for Consecutive Characters.
# Memory Usage: 13.7 MB, less than 10.43% of Python online submissions for Consecutive Characters.
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = s[0]
        counter = 1
        max_counter = 1
        for ch in s[1:]:
            if ch == prev:
                counter += 1
            else:
                if max_counter < counter:
                    max_counter = counter
                counter = 1
                prev = ch
        if max_counter < counter:
            max_counter = counter
        return max_counter