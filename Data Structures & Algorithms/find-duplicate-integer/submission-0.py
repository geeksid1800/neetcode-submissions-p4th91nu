''' Listing the solution only for O(1) SC without modifiying nums: Loop Detection method ==>
If we treat nums like a linked list, where the value v at an index i (nums[i] = v) 
means that the node with ID 'i' points to (has as 'next') the node with ID 'v',
then we notice something useful.
1) Since all values in nums are in [1,n], no node will point to node ID '0', so this is
always a/the start of the linked list.
2) Since there are n+1 nodes but at max only 'n' possible values of 'next', and since one
element is guaranteed to be repeated (atleast twice), it means that element has atleast 2
nodes pointing to it. That means if you traverse the LL, you will eventually revisit a
position you've already been to (the second time a node points to that repeated element). 
3) Once you revisit a node, it means you are in a loop, since it has only one possible next
node and you are on the same path you've already taken. 
4) Also, the element with multiple nodes pointing to it is the start of the loop, 
as it has (atleast) the non-loop part of the LL and the loop part both pointing to it.
However, recall that a node 'v' is being pointed to by node 'i' if nums[i] = v.
So if 'x' has multiple nodes pointing to it, it means there are multiple i1,i2.. such that
nums[i] = x, i.e. 'x' is the repeated element. So finding the start of the loop will give us
the repeated element.
From here onwards, use the slow-fast pointer technique to find the start of the loop.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]; fast = nums[fast]

            if slow == fast: break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow