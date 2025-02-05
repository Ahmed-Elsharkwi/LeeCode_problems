# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, first, second):
        if first is None and second is None:
            return True
        if (first != None and second != None) and (first.val == second.val):
            result = self.fun(first.left, second.right)
            if result:
                result = self.fun(first.right, second.left)
        else:
            return False

        return result
   
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.fun(root.left, root.right)
