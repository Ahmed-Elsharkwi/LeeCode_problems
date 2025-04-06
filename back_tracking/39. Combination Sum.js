/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let new_array = [];
    
    function recursion(i, new_list){
        let result = 0;
        for (let e of new_list){
            result += e;
        }
        if (result == target){
            new_array.push(new_list);
            return;
        }
        if (( i == candidates.length) || (result > target)){
            return;
        }
        recursion(i, new_list.concat([candidates[i]]));
        recursion(i + 1, new_list);
    }
    recursion(0, []);
    return new_array;
};
