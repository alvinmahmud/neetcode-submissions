# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        previous_group = dummy

        while True:
            kth = self.getKth(previous_group, k)
            if not kth:
                return dummy.next
            next_group = kth.next

            prev, curr = kth.next, previous_group.next
            while curr != next_group:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            temp = previous_group.next
            previous_group.next = kth
            previous_group = temp
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr