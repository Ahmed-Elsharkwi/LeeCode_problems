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
 * @return {boolean}
 */
function fun(p){
    if (p.left == null && p.right == null){
        return [0, true];
    }
    let left_count = [0, true];
    let right_count = [0, true];

    if (p.left){
        left_count = fun(p.left);
        left_count[0] += 1;
        if (left_count[1] == false){
            return left_count;
        }
    }
    if (p.right){
        right_count = fun(p.right);
        right_count[0] += 1;
        if (right_count[1] == false){
            return right_count
        }
    }
    if (Math.abs(left_count[0] - right_count[0]) < 2){
        return [Math.max(left_count[0], right_count[0]), true];
    }
    return [left_count[0], false];
}
var isBalanced = function(root) {
    if ((root == null) || (root.left == null && root.right == null)){
        return true;
    }
    return fun(root)[1];
};
