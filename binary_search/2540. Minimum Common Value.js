/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    let nums3 = [];
    let nums4 = [];
    let flag = 0;
    let num = -1;

    if (nums1.length > nums2.length) {
        nums3 = nums1;
        nums4 = nums2;
    }
    else {
        nums3 = nums2;
        nums4 = nums1;
    }

    for (let i = 0; i < nums3.length; i++) {
        let right = nums4.length - 1;
        let left = 0;

        if (nums3[i] < num || flag == 0) {

            while (left <= right) {
                let mid = parseInt((left + right) / 2);

                if (nums4[mid] == nums3[i]) {
                    flag = 1;
                    num = nums4[mid];
                    break;
                }
                else if (nums4[mid] > nums3[i]) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }
        }
    }
    return num;
};
