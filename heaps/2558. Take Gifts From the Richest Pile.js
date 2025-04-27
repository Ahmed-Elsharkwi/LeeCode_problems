/**
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */

function heapfy(array, n, i){    
    let left = (2 * i) + 1;
    let right = (2 * i) + 2;
    let largest = i;

    if ((left < n) && (array[left] > array[largest])){
        largest = left;
    }
    if ((right < n) && (array[right] > array[largest])){
        largest = right;
    }

    if (largest != i){
        [array[largest], array[i]] = [array[i], array[largest]];
        heapfy(array, array.length, largest);
    }
    
}
function loop(array){
    let i = parseInt(array.length / 2) - 1;

    while (i >= 0){
        heapfy(array, array.length, i);
        i -= 1;
    }
    
}
var pickGifts = function(gifts, k) {
    while (k > 0){
        loop(gifts);
        let num = gifts.shift();
        gifts.push(parseInt(Math.sqrt(num)));
        k -= 1;
    }
    return gifts.reduce((total, number) => total + number, 0)
};
