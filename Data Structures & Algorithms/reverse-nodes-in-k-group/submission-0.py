# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        ix = 0
        curr = head
        beforeLeft = root
        while curr:
            if ix > 0 and ix%k == 0:
                #we reached the end of a segment to be reversed. Reverse [beforeLeft.next to curr-1]
                left = beforeLeft.next #the first node that is part of the segment to be reversed
                prev, front = beforeLeft, left
                while front and front != curr:
                    nxt = front.next
                    front.next = prev
                    prev, front = front, nxt
                beforeLeft.next = prev
                if left:
                    left.next = front
                
                beforeLeft = left 
                '''next segment to be potentially reversed starts at curr/front
                left is now the node before that'''

            ix += 1
            curr = curr.next

        
        #check if curr has reached None at end of LL, but we have also completed another k-segment
        
        if ix > 0 and ix%k == 0:
            #we reached the end of a segment to be reversed. Reverse [beforeLeft.next to curr-1]
            left = beforeLeft.next #the first node that is part of the segment to be reversed
            prev, front = beforeLeft, left
            while front and front != curr:
                nxt = front.next
                front.next = prev
                prev, front = front, nxt
            beforeLeft.next = prev
            if left:
                left.next = front
            
            beforeLeft = left 
            '''next segment to be potentially reversed starts at curr/front
            left is now the node before that'''
        

        return root.next
