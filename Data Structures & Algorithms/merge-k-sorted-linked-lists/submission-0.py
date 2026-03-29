import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
There exists an obvious recursive method, where at any point you take 2 LinkedLists, where atleast
one is non-null, and do the standard, 'Merge 2 sorted LLs', and then take the halved in number LLs 
and repeat, until there is only one Linked List remaining. 
Basic logic is to implement 'Merge 2 sorted LLs' as a subproblem, then iterate over 'lists' 2 at a time,
pick list[i] and list[i+1], merge them, store the merged head in mergedLists. 
At the end of iterating thru lists, make lists = mergedLists and recur.

Another logic is to maintain a priority queue/minheap, since at any point we only need the minimum of
all current nodes from all the lists. Initially heap/pq will consist of all the 'heads'.
At any point, pop the minimum node, add it to the final result, and push it's next node (if it exists)
back into pq.
I prefer this method, as less mucking about in recursion, but we have to define our custom __lt__() for
comparing two nodes on the basis of their values. For this we subclass ListNode. 
'''

class CustomListNode(ListNode):
    def __init__(self, node):
        super().__init__(node.val, node.next)
        self.node = node
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        curr = root = ListNode()
        minheap = []

        for head in lists:
            if head:
                minheap.append(CustomListNode(head))

        heapq.heapify(minheap)

        while minheap:
            currMin: CustomListNode = heapq.heappop(minheap)
            minNode: ListNode = currMin.node
            curr.next = minNode
            curr = curr.next
            if minNode.next:
                heapq.heappush(minheap, CustomListNode(minNode.next))
            
        return root.next