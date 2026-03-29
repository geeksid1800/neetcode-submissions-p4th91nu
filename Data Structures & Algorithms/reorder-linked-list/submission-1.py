'''
Basic logic is to split the nodes into two halves,
reverse the second half
and then alternately add the second half nodes in between the first half ones
Eg 1->2->3->4 => (1->2) and (3->4) => (1->2) and (4->3) => 1->4->2->3
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        split the list into halves -> if there are 4 nodes, 2 and 2. For 5, 3 and 2
        i.e. first half has (n+1)//2 nodes
        '''
        prev = ListNode(0,head) #add 1 node so that we have (n+1) nodes
        slow = fast = prev
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        lastLeft = slow #when loop exits, slow will be on the last node of left side
        firstRight = lastLeft.next

        '''Now reverse the right half and add it alternately in between the left side nodes
        Eg 1->2->3->4 => (1->2) and (3->4) => (1->2) and (4->3) => 1->4->2->3'''

        lastLeft.next = None #break the link between the two lists

        prev, curr = None, firstRight
        while curr:
            nxt = curr.next
            curr.next = prev
            curr, prev = nxt, curr


        l, r = head, prev #pre points to last node (in original order)
        while r: #since left side has greater than or equal no. of nodes than right side
            nxt = l.next
            l.next = r
            l = nxt

            nxt = r.next
            r.next = l
            r = nxt
        
        