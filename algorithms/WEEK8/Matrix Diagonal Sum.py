"""
1572. Matrix Diagonal Sum
Easy
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

"""
#2 solutions
 
# Runtime: 80 ms, faster than 92.79% of Python online submissions for Matrix Diagonal Sum.
# Memory Usage: 13.6 MB, less than 41.89% of Python online submissions for Matrix Diagonal Sum.
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
            s += mat[i][len(mat) - 1 - i]
        if len(mat) % 2 == 1:
            s -= mat[len(mat) // 2][len(mat) // 2]
        return s




# Runtime: 88 ms, faster than 55.41% of Python online submissions for Matrix Diagonal Sum.
# Memory Usage: 13.5 MB, less than 95.27% of Python online submissions for Matrix Diagonal Sum. class Solution(object):
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s = 0
        l = len(mat)
        s += sum([mat[i][i] for i in range(l)])
        s += sum([mat[i][l - 1 - i] for i in range(l)])
        if len(mat) % 2 == 1:
            s -= mat[l // 2][l // 2]
        return s