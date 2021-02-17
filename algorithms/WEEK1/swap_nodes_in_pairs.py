"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev_cur = ListNode()
        if head == None:
            return head
        if head.next == None:
            return head
        new_head = head.next
        while current:
            current1 = current.next
            if current1 != None:#case for odd length
                current2 = current1.next
            else:
                break
            current.next = current2
            current1.next = current
            prev_cur.next = current1
            prev_cur = current
            current = current.next
            
        return new_head
            