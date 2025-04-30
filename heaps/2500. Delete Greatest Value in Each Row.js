/**
 * @param {number[][]} grid
 * @return {number}
 */
var heapfy = function(list, n, i){
    let left = (i * 2) + 1;
    let right = (i * 2) + 2;
    let largest = i;

    if ((left < n) && (list[left] > list[largest])){
        largest = left;
    }
    if ((right < n) && (list[right] > list[largest])){
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
var deleteGreatestValue = function(grid) {
    let total = 0;
    let length = grid[0].length;

    while (length > 0){
        let tmp = 0;

        for (let i = 0; i < grid.length; i++){
            loop(grid[i]);
            let number = grid[i].shift();
            if (number > tmp){
                tmp = number;
            }
        }
        total += tmp;
        length -= 1;
    }
    return total;

};
