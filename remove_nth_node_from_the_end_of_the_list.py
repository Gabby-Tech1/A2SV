# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head

        for _ in range(n):
            first = first.next
        print(first)
        
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return head
        