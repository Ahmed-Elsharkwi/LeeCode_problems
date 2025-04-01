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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    let new_array = [];

    function iterate(string, root) {
        string += `${root.val}`;
        if ((root.left == null) && (root.right == null)){
            new_array.push(string);
            return;
        }
        string += "->";

        if (root.left != null){
            iterate(string, root.left);
        }
        if (root.right != null){
            iterate(string, root.right);
        }
    }
    iterate("", root);
    return new_array;
};
