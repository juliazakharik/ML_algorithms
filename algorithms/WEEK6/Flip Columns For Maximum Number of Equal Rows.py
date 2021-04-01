"""
1072. Flip Columns For Maximum Number of Equal Rows
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

"""
# Runtime: 1596 ms, faster than 36.67% of Python online submissions for Flip Columns For Maximum Number of Equal Rows.
# Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for Flip Columns For Maximum Number of Equal Rows.
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        max_counter = 0
        flip = {1 : 0, 0 : 1}
        l, l1 = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            tr = [flip[row[j]] for j in range(l1)]
            counter = len([1 for j in range(i, l) if matrix[j] == row or matrix[j] == tr])
            if counter > max_counter:
                max_counter = counter
        return max_counter
                