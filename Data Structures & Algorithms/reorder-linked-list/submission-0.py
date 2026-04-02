# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        prev, cur = None, mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        start, end = head, prev
        while end.next:
            nxt1 = start.next
            start.next = end
            start = nxt1

            nxt2 = end.next
            end.next = start
            end = nxt2