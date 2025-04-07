/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    let outer_array = [];
    candidates.sort();

    function dfs(i, new_list){
        let result = 0;
        for (let e of new_list){
            result += e;
        }
        if (result == target){
            outer_array.push(new_list)
            return true;
        }
        if ((i == candidates.length) || (result > target)){
            return false;
        }
        dfs(i + 1, new_list.concat([candidates[i]]))
        
        while ((i < candidates.length) && (candidates[i] == candidates[i + 1])){
            i += 1;
        }
        dfs(i + 1, new_list)

    }

    dfs(0, []);
    return outer_array
};
