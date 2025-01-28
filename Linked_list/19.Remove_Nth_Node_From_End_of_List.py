# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        back,front  = head, head
        third = None

        while n > 0 and front:
            n -= 1
            front = front.next

        while front != None:
            third = back
            back = back.next
            front = front.next
        if third is None:
            head = head.next
        else:
            third.next = back.next
        return head

        
