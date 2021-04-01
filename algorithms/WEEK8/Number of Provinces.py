"""
547. Number of Provinces
Medium
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
#2 solutions

# Runtime: 160 ms, faster than 65.04% of Python online submissions for Number of Provinces.
# Memory Usage: 13.8 MB, less than 75.12% of Python online submissions for Number of Provinces.
class Solution(object):
    def dfs(self, isConnected, start, visitList, stack):
        if visitList[start] == 0:
            visitList[start] = 1
            stack.append(start)
        for i in range(len(isConnected)):
            if isConnected[start][i] == 1 and visitList[i] == 0:
                self.dfs(isConnected, i, visitList, stack)
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visitList = [0] * len(isConnected)
        stack = []
        vertex = 0
        counter = 0
        while sum(visitList) < len(isConnected):
            self.dfs(isConnected, vertex, visitList, stack)
            counter += 1
            for i in range(len(visitList)):
                if visitList[i] == 0:
                    vertex = i
                    break
        return counter





# Runtime: 148 ms, faster than 96.22% of Python online submissions for Number of Provinces.
# Memory Usage: 13.7 MB, less than 89.45% of Python online submissions for Number of Provinces.
class Solution(object):
    def dfs(self, isConnected, start, visitList, stack):
        
        del visitList[start]
        stack.append(start)
        for i in range(len(isConnected)):
            if isConnected[start][i] == 1 and i in visitList:
                self.dfs(isConnected, i, visitList, stack)
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visitList = {}
        for i in range(len(isConnected)):
            visitList[i] = 0
        stack = []
        counter = 0
        while len(visitList) > 0:
            vertex = visitList.keys()[0]
            self.dfs(isConnected, vertex, visitList, stack)
            counter += 1
            
        return counter