"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        current1 = l1
        current2 = l2
        remember = 0 #if sum > 10
        sum_cur = current1.val + current2.val + remember
        if sum_cur < 10:
            resNode = ListNode(sum_cur)
            remember = 0
        else:
            resNode = ListNode(sum_cur % 10)
            remember = 1
        res = resNode
        head = res # head of result linked list
        while current1.next or current2.next:
            if not current1.next:
                resNode = ListNode(0)
                current1.next = resNode
            current1 = current1.next
            if not current2.next:
                resNode = ListNode(0)
                current2.next = resNode
            current2 = current2.next
            sum_cur = current1.val + current2.val + remember
            
            if sum_cur < 10:
                resNode = ListNode(sum_cur)
                remember = 0
            else:
                resNode = ListNode(sum_cur % 10)
                remember = 1
            res.next = resNode
            res = res.next
        if remember == 1:
            resNode = ListNode(remember)
            res.next = resNode
        return head
        