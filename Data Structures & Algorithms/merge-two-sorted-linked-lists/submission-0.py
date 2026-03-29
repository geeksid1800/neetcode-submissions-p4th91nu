# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        head = curr = ListNode()

        while p1 and p2:
            if p1.val < p2.val:
                newNode = ListNode(val=p1.val)
                p1 = p1.next
            else:
                newNode = ListNode(val=p2.val)
                p2 = p2.next
            curr.next = newNode
            curr = curr.next
        
        while p1:
            newNode = ListNode(val=p1.val)
            p1 = p1.next
            curr.next = newNode
            curr = curr.next

        while p2:
            newNode = ListNode(val=p2.val)
            p2 = p2.next
            curr.next = newNode
            curr = curr.next

        return head.next