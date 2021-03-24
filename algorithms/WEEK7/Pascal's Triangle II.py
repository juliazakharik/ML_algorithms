"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

"""

# Runtime: 12 ms, faster than 96.83% of Python online submissions for Pascal's Triangle II.
# Memory Usage: 13.5 MB, less than 14.46% of Python online submissions for Pascal's Triangle II.
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        old_arr = [1,1]
        new_arr = old_arr
        for i in range(2, rowIndex + 1):
            new_arr = [1]
            for j in range(len(old_arr) - 1):
                new_arr.append(old_arr[j] + old_arr[j+1])
            new_arr.append(1)
            old_arr = new_arr
        return new_arr