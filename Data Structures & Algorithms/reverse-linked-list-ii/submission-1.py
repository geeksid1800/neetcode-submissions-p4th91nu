'''
Traverse the LL and maintain an index,
when index is between left and right, do the standard reversal of LL
Then join the node before old 'left' to the last node that has been reversed ('prev' after reversal).
Also join the index that was originally at index 'left' to the first node after the reversed section
('curr' after reversal).
I am going to show this with example of [1,2,3,4,5], left = 2, right = 3
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ix = 1
        prev = root = ListNode(0,head)
        curr = head

        while curr and ix < left:
            prev = curr
            curr = curr.next
            ix += 1
        
        #now ix == left
        beforeLeft = prev
        '''
        [0->1->2->3->4->5], beforeLeft = 1, prev = 1, curr = left = 2
        '''
        while curr and ix <= right:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
            ix += 1
        '''
        [0->1<=>2<-3 4->5], beforeLeft=1, prev = 3, curr = 4
        '''
        #now prev points to last node reversed, curr points to first node after it
        beforeLeft.next.next = curr
        '''
        [0->1->2->4->5] beforeLeft=1, beforeLeft.next = 2, prev = 3, curr = 4
               ^
               |
               3
        '''
        beforeLeft.next = prev
        '''
        [0->1->3->2->4->5]
        '''
        return root.next
