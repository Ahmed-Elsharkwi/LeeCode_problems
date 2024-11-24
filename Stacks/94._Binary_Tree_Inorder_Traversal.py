# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        new_list = []
        if root is None:
            return new_list
        def inorder(root, new_list):
            if root.left is not None:
                new_list = inorder(root.left, new_list)
            new_list.append(root.val)
            if root.right is not None:
                new_list = inorder(root.right, new_list)
            return new_list
        return inorder(root, new_list)

