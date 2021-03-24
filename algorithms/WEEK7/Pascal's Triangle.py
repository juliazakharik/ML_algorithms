"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""

# Runtime: 20 ms, faster than 49.36% of Python online submissions for Pascal's Triangle.
# Memory Usage: 13.1 MB, less than 99.40% of Python online submissions for Pascal's Triangle.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        old_arr = [1,1]
        for i in range(2, numRows):
            new_arr = [1]
            for j in range(len(old_arr) - 1):
                new_arr.append(old_arr[j] + old_arr[j+1])
            new_arr.append(1)
            old_arr = new_arr
            res.append(new_arr)
        return res