"""
606. Construct String from Binary Tree
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 44 ms, faster than 48.31% of Python online submissions for Construct String from Binary Tree.
# Memory Usage: 16.3 MB, less than 39.89% of Python online submissions for Construct String from Binary Tree.
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)+''
        if not t.right:
            return str(t.val) + '(' + str(self.tree2str(t.left)) + ')'
        return str(t.val) + '(' + str(self.tree2str(t.left)) + ')' + '(' + str(self.tree2str(t.right)) + ')'
            
        