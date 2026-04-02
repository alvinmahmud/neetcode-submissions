# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        if l == n: return head.next
        
        curr = head
        for _ in range(l - 1 - n):
            curr = curr.next
        curr.next = curr.next.next

        return head