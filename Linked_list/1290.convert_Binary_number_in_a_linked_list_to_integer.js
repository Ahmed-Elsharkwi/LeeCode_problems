/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
    let num_bit = "";
    let holder = head;
    let decimal_num = 0;

    while (holder != null) {
        num_bit += holder.val;
        holder = holder.next;
    }
    i = 0
    for (let num = (num_bit.length - 1); num >= 0; num--) {
        decimal_num += (2**i * +(num_bit[num]))
        i++;
    }
    return decimal_num;
};
