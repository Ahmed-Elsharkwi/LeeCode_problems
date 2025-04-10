/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    
    outer_array = [];

    function backtracking(start, list){
        if (list.length == k){
            outer_array.push(list);
            return;
        }
        for (let j = start; j <= n; j++){
            backtracking(j + 1, list.concat([j]));
        }
    }
    backtracking(1, []);
    return outer_array;
};
