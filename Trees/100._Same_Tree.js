/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (p == null && q == null) {
        return true;
    }
    if ((p != null && q != null) && (p.val == q.val)){
        result = true;
        result = isSameTree(p.left, q.left);
        if (result == true){
            result = isSameTree(p.right, q.right);
        }
    }
    else {
        return false;
    }

    
    return result
};
