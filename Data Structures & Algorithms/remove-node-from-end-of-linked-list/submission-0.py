# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        root = prev = ListNode(0,head)
        curr = head
        ix = 0
        while ix != (count - n):
            ix += 1
            prev = curr
            curr = curr.next
        #now we are at the index to be removed
        prev.next = curr.next

        return root.next