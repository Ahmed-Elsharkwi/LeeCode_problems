/**
 * @param {number[]} nums
 * @return {number[]}
 */
var heapfy = function(list, n, i){
    let left = (i * 2) + 1;
    let right = (i * 2) + 2;
    let largest = i;

    if ((left < n) && (list[left] < list[largest])){
        largest = left;
    }
    if ((right < n) && (list[right] < list[largest])){
        largest = right;
    }
    if (largest != i){
        [list[largest], list[i]] = [list[i], list[largest]];
        heapfy(list, n, largest);
    }
}
var loop = function(list){
    let i = parseInt(list.length / 2) - 1;
    while (i >= 0){
        heapfy(list, list.length, i);
        i -= 1;
    }
}
var numberGame = function(nums) {
    let length = nums.length;
    let bob = 0;
    let alice = 0;
    let answer = [];
    
    while (length > 0){
        loop(nums);
        alice = nums.shift();
        loop(nums);
        bob = nums.shift();
        answer.push(bob, alice);
        length -= 2;
    }
    return answer;
};
