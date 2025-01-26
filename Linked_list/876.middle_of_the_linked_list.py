# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        count = 0
        while pointer != None:
            count += 1
            pointer = pointer.next

        mid = count // 2
        i = 0
        pointer = head

        while i != mid:
            pointer = pointer.next
            i += 1

        return pointer
