# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        # Check if we need to reverse the group (if there are less than k nodes, LL remains unchanged)
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we want that `head` is the end of the group, so it's next should point to
        # the start of the next k-segment. 
		# And `curr` is the next pointer in original linked list order (i.e. start of next k-group)
        head.next = self.reverseKGroup(curr, k)
        return prev