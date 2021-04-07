"""
532. K-diff Pairs in an Array
Medium
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

"""
# Runtime: 60 ms, faster than 75.39% of Python online submissions for K-diff Pairs in an Array.
# Memory Usage: 16.1 MB, less than 12.95% of Python online submissions for K-diff Pairs in an Array.
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if k == 0:
        #     return len(nums) - len(list(set(nums)))
        d = defaultdict(list)
        
        count = 0
        if k == 0:
            for num in nums:
                if num in d and d[num] == 0:
                    count += 1
                    d[num] = 1
                if num not in d:
                    d[num] = 0
            return count
            
        for num in nums:
            d[num] = [k + num, num - k]
            
        for key in d.keys():
            if d[key][0] in d:
                count += 1
            if d[key][1] in d:
                count += 1
            del d[key]
            
        return count
        