/**
 * @param {number[]} stones
 * @return {number}
 */
function heapfy(arr, n, i){
    let l = (2 * i) + 1;
    let r = (2 * i) + 2;
    let largest = i;

    if ((l < n) && (arr[l] >= arr[largest])){
        largest = l;
    }
    if ((r < n) && (arr[r] > arr[largest])){
        largest = r;
    }

    if (largest != i){
        [arr[largest], arr[i]] = [arr[i], arr[largest]];
        heapfy(arr, n, largest);
    }
}
function loop(arr){
    let index = (parseInt(arr.length / 2) - 1);

    while (index >= 0){
        heapfy(arr, arr.length, index);
        index -= 1;
    }
}
var lastStoneWeight = function(stones) {
    let length = stones.length;
    let tmp = 0;

    while (length > 1){
        loop(stones);
        let first_num = stones.shift();
        
        if (stones[0] < stones[1]){
            [stones[0], stones[1]] = [stones[1], stones[0]];
        }
        let second_num = stones.shift();

        if (first_num != second_num){
            stones.push(Math.abs(first_num - second_num));
            length += 1;
        }
        length -= 2;
    }
    
    if (stones.length == 1){
        return stones[0];
    }
    return 0;
};
