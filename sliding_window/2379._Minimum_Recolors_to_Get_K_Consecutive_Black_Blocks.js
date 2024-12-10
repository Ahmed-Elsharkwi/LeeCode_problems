/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    let left = 0;
    let count_w = 0;
    let count_b = 0;
    let flag = 0;

    for (let right = k - 1; right < blocks.length; right++) {
        let idx = left;
        let count = 0;
        count_b = 0;
        while (idx <= right && count < k) {
            if (blocks[idx] == 'W') {
                count += 1
            }
            else {
                count_b += 1;
            }
            idx += 1;
        }
        if (flag == 0) {
            count_w = count;
            flag = 1;
        }
        else {
            count_w = Math.min(count, count_w);
        }
        if (count_b == k) {
            return 0;
        }
        left += 1;
    }
    return count_w;
    
};
