/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumStrongPairXor = function(nums) {
    let left = 1;
    let right = 0;
    let flag = 0;

    let count_1 = nums[0] ^ nums[0];

    while (right < nums.length) {
        if (flag == 1) {
            left = right;
        }
        while (left < nums.length) {
            if (Math.abs(nums[left] - nums[right]) <= Math.min(nums[left], nums[right])) {
                count_1 = Math.max(count_1, (nums[left] ^ nums[right]));

                console.log(nums[left], nums[right], count_1)
            }
            left += 1;
        }
        if (flag == 0) {
            flag = 1;
        }
        right += 1;
    }
    return count_1;
};
