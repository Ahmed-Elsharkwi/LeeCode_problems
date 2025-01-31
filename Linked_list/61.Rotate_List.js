/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    let first = head;
    let second = head;
    let result = 0;
    third = null;
    let length = 0;

    if (head == null || head.next == null) {
        return head;
    }

    while (first.next != null) {
        length += 1;
        first = first.next;
    }
    length += 1

    k = k % length
    
    while (k > 0) {
        first = head;

        while (first.next.next != null) {
            first = first.next;
        }
        first.next.next = head;
        head = first.next;
        first.next = null;
        k -= 1;
    }
    return head
};
