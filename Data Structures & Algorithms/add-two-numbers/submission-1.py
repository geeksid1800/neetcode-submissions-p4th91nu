# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0

        curr = root = ListNode()

        while p1 and p2:
            s = p1.val + p2.val + carry
            newNode = ListNode(s%10, None)
            curr.next = newNode
            carry = s//10
            curr = curr.next
            p1, p2 = p1.next, p2.next
        
        while p1:
            s = p1.val + carry
            newNode = ListNode(s%10, None)
            curr.next = newNode
            carry = s//10
            curr = curr.next
            p1 = p1.next

        while p2:
            s = p2.val + carry
            newNode = ListNode(s%10, None)
            curr.next = newNode
            carry = s//10
            curr = curr.next
            p2 = p2.next
        
        if carry:
            newNode = ListNode(carry, None)
            curr.next = newNode
        
        return root.next