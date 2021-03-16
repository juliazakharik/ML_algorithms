"""
274. H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

"""

#Runtime: 28 ms, faster than 48.65% of Python online submissions for H-Index.
# Memory Usage: 13.5 MB, less than 92.79% of Python online submissions for H-Index.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #citations = sorted(citations)
        citations.sort()#faster than sorted()
        h = citations[0]
        for i in range(1, len(citations)+1):
            if citations[-i]  >= i -1:
                h = min(i, citations[-i])
        return h