"""
941. Valid Mountain Array
Easy
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false

"""
# Runtime: 172 ms, faster than 50.45% of Python online submissions for Valid Mountain Array.
# Memory Usage: 14.7 MB, less than 45.29% of Python online submissions for Valid Mountain Array.
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l = len(arr)
        if l < 3:
            return False
        remember = 0
        for i in range(l - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif arr[i + 1] < arr[i]:
                remember = i + 1
                break
        if remember == 1 or remember == 0:
            return False
        for i in range(remember, l - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif arr[i + 1] > arr[i]:
                return False

        return True



