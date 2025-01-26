/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    let first = head;
    let second = null;
    let third = null;

    while (first != null) {
        second = first.next;
        if (first.val == val) {
            if (first == head) {
                head = second;

            }
            else {
                third.next = first.next;
            }
            first.next = null;
        }
        else{
            third = first;
        }
        first = second;
    }
    return head;
};
