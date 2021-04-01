"""
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

# Runtime: 16 ms, faster than 82.09% of Python online submissions for Unique Paths.
# Memory Usage: 13.2 MB, less than 92.99% of Python online submissions for Unique Paths.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # matr = [[1] * n] * m
        # matr = [[1 for i in range(n)] for j in range(m)]
        matr = []
        for i in range(m):
            mt = []
            for j in range(n):
                mt.append(1)
            matr.append(mt)
        
        for i in range(1, m):
            for j in range(1, n):
                matr[i][j] = matr[i - 1][j] + matr[i][j - 1]
        return matr[m - 1][n - 1]