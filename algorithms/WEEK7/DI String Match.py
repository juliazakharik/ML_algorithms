"""
942. DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
"""

#Runtime: 48 ms, faster than 88.94% of Python online submissions for DI String Match.
# Memory Usage: 14.8 MB, less than 58.06% of Python online submissions for DI String Match.
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start, end = 0, len(S)
        res = []
        
        for letter in S:
            if letter == "I":
                
                res.append(start)
                start += 1
            else:
                
                res.append(end)
                end -= 1
        res.append(start)
        return res
        