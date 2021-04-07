"""
1721. Swapping Nodes in a Linked List
Medium
Share
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        current = head
        first = head
        second = head 
        while current:
            if count == k:
                first = current
            current = current.next
            count += 1
        l = count 
        current = head
        count = 0
        while current:
            if l - count - 1== k:
                second = current
            current = current.next
            count += 1
        first.val, second.val = second.val, first.val
        return head
        

