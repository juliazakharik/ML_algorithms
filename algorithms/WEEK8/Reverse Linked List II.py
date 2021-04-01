"""
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]


"""

# Runtime: 16 ms, faster than 85.75% of Python online submissions for Reverse Linked List II.
# Memory Usage: 13.7 MB, less than 59.81% of Python online submissions for Reverse Linked List II.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        c = 1
        arr = []
        current = head
        print(type(left))
        while current:
            if c >= left and c <= right:
                arr.append(current.val)
            c += 1
            current = current.next
        current = head
        arr = arr[::-1]
        c = 1
        while current:
            if c >= left and c <= right:
                current.val = arr[c - left]
            c += 1
            current = current.next
        return head