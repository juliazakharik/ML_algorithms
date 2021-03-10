"""
493. Reverse Pairs
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
"""

#O(n^2)
#don't work for all test cases
class Solution(object):
    #Time Limit Exceeded
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    counter += 1
        return counter



#(O(n))
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count_ge = 1
        
        
class BST:
    def __init__(self, val):
        self.head = Node(val)
        
    def search(self, val):
        current = self.head
        while current:
            if val > current.val:
                current = current.right
            elif val < current.val:
                current = current.left
            else:
                return current.count_ge
        return 0
    
    def add(self, val):
        current = self.head
        if self.head == None:
            self.head = Node(val)
            return
        while current:
            
            print(current.val, current.count_ge, val, current.val)
            if val > current.val:
                current.count_ge += 1

                if not current.right:
                    current.right = Node(val)
                    break
                else:
                    current = current.right
            elif val < current.val:
                if not current.left:
                    current.left = Node(val)
                    break
                else:
                    current = current.left
            else:
                current.count_ge += 1
                return 
class Solution(object):
    def reversePairs(self, nums):
        counter = 0
        bst = BST(nums[0])
        for num in nums[1:]: 
            print(num)
            counter += bst.search(2 * num + 1)
            bst.add(num)
        return counter



#O(nlogn)
class Solution(object):
    
    def binary_search(self, arr, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1
 
    def reversePairs(self, nums):
        nums = sorted(nums)
        counter = 0
        l = len(nums)
        for i in range(len(nums)):
            counter += (l - binary_search(nums, 0, l - 1, 2 * nums[i] + 1))
        return counter
            