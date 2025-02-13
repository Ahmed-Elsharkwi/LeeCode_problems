# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cal_path(self, root, targetSum, total_sum):
        print(root.right)
        if (root.left is None) and (root.right is None):
            if ((total_sum + root.val) == targetSum):
                return True
            else:
                return False

        total_sum += root.val
        if root.left:
            result = self.cal_path(root.left, targetSum, total_sum)
            if result is True:
                return result
    
        if root.right:
            result = self.cal_path(root.right, targetSum, total_sum)
            if result is True:
                return result
        
        total_sum -= root.val
        return False
            
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.cal_path(root, targetSum, 0)
