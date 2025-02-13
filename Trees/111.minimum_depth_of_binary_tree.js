/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    let left_count = 0;
    let right_count = 0;

    if (root == null){
        return 0;
    }

    if (root.left == null && root.right == null){
        return 1;
    }
    if (root.left != null){
        left_count = minDepth(root.left) + 1;
    }
    if (root.right != null){
        right_count = minDepth(root.right) + 1;
    }
    if (left_count == 0 || right_count == 0){
        return Math.max(right_count, left_count);
    }
    return Math.min(right_count, left_count);
};
