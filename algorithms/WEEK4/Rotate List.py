
"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

"""




#Runtime: 24 ms, faster than 75.09% of Python online submissions for Rotate List.
#Memory Usage: 13.3 MB, less than 98.66% of Python online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head == None or head.next == None:
            return head

        l = 0
        current = head
        tail = head
        while current:
            l += 1
            if not current.next:
                tail = current
            current = current.next


        k = k % l
        if k == 0:
            return head
        current = head
        i = 0
        first = head
        while current:
            if i == l - k - 1:
                first = current.next
                current.next = None
            current = current.next
            i += 1
        tail.next = head
        head = first
        return head
