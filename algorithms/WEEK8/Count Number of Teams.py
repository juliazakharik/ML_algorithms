"""
1395. Count Number of Teams
Medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

"""
# Runtime: 1520 ms, faster than 21.16% of Python online submissions for Count Number of Teams.
# Memory Usage: 30.2 MB, less than 5.39% of Python online submissions for Count Number of Teams.
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        greater = {}
        less = {}
        
        for i in range(len(rating)):
            greater[i] = []
            less[i] = []
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i].append(j)
                else:
                    less[i].append(j)

        num_teams = 0
        for i in range(len(rating)):
            for j in greater[i]:
                num_teams += len(greater[j])
            for j in less[i]:
                num_teams += len(less[j])

        return num_teams