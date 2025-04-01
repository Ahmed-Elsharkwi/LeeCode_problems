/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums) {
    function iterate(index, total){
        if (index == nums.length){
            return total;
        }
        return iterate(index + 1, total ^ nums[index]) + iterate(index + 1, total);   
    }
    return iterate(0, 0);
};
