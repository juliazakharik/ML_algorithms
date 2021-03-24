"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""

# Runtime: 292 ms, faster than 97.19% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 23.4 MB, less than 22.02% of Python online submissions for Find All Duplicates in an Array.
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        d={}
        for num in nums:
            if num in d:
                res.append(num)
            else:
                d[num] = 0
        return res



# Runtime: 300 ms, faster than 92.38% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 22.4 MB, less than 25.17% of Python online submissions for Find All Duplicates in an Array
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        d=set()
        for num in nums:
            if num in d:
                res.append(num)
            else:
                d.add(num)
        return res
        


# Runtime: 312 ms, faster than 80.30% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 20.5 MB, less than 78.64% of Python online submissions for Find All Duplicates in an Array.
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] *= (-1)
        return res



# Runtime: 324 ms, faster than 55.91% of Python online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 20.7 MB, less than 82.90% of Python online submissions for Find All Numbers Disappeared in an Array.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= (-1)
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res


# Runtime: 288 ms, faster than 96.46% of Python online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 20.8 MB, less than 70.01% of Python online submissions for Find All Numbers Disappeared in an Array.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        l = len(nums)
        for num in nums:
            nums[num % l - 1] += l
        for i in range(l):
            if nums[i]<=l:
                res.append(i+1)
        return res
    
    
        
        