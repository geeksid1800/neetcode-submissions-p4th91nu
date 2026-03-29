# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        ix = 1
        curr = head
        beforeLeft = root
        while curr:
            if ix%k == 0:
                #we reached the end of a segment to be reversed. Reverse [beforeLeft.next to curr]
                next_group = curr.next
                left = beforeLeft.next #the first node that is part of the segment to be reversed
                prev, front = beforeLeft, left
                while front and front != next_group:
                    nxt = front.next
                    front.next = prev
                    prev, front = front, nxt
                beforeLeft.next = prev
                if left:
                    left.next = front
                
                curr = beforeLeft = left 
                '''next segment to be potentially reversed starts at front/next_group and
                left is now the node before that
                Also move curr there so we can continue with the overall loop. 
                '''

            ix += 1
            curr = curr.next

        return root.next
