# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        prev, curr = root, head

        for i in range(n):
            curr = curr.next
        
        early = curr
        prev, curr = root, head
        while early:
            early = early.next
            prev = curr
            curr = curr.next
        
        #when early reaches None, curr is at the element to be removed
        prev.next = curr.next
        return root.next