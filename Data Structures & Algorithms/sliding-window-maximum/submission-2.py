from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        If we maintain a candidate (for max in current window) and it's index,
        everytime we get a number that is larger than the current candidate
        and also after it (index-wise),
        the candidate will no longer be the soln for any window henceforth,
        so we can remove it from list of candidates.
        In that spirit, maintain a deque with (val, index).
        Remove an item/items from deque if we get a larger val, or if it's
        index is outside of permissible values for the window.

        We can also use a priority queue (see earlier accepted submission),
        but that would be O(nlogn), and deque is O(n) TC. 
        '''
        
        dq = deque()
        l=0
        ans = []

        for r in range(len(nums)):
            curr = (nums[r],r) #curr[0] = val, curr[1] = ix
            while len(dq) and (dq[-1][0] <= nums[r]):
                #keep removing elements from the end as long as they're smaller
                dq.pop()
            dq.append(curr)

            if r-l+1 < k:
                continue #not gotten a full window yet
            
            if dq[0][1] < l:
                dq.popleft()
                #since window moves only 1 position at a time, at max one
                # val in the deque will be outside the window
            
            ans.append(dq[0][0])
            l += 1
        
        return ans