"""
1497. Check If Array Pairs Are Divisible by k
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.
Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

"""

#Runtime: 612 ms, faster than 60.32% of Python online submissions for Check If Array Pairs Are Divisible by k.
# Memory Usage: 27.8 MB, less than 57.14% of Python online submissions for Check If Array Pairs Are Divisible by k.
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(len(arr)):
            k1 = arr[i] % k
            if k1 in d:
                d[arr[i] % k] += 1
            else:
                d[arr[i] % k] = 1
                
        if 0 in d:
            if d[0] % 2 != 0: return False
            del d[0]
        
        for key in d:
            k1 = k - key
            if k1 in d:
                if d[key] != d[k1]:
                    return False
                # else:
                #     del d[key]
                #     del d[k1]
            else:
                return False   
        return True
