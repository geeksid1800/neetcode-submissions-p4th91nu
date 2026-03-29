import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        If we maintain a candidate (for max in current window) and it's index,
        everytime we get a number that is larger than the current candidate
        and also after it (index-wise),
        the candidate will no longer be the soln for any window henceforth,
        so we can remove it from list of candidates.
        In that spirit, maintain a priority queue with (val, index).
        Remove an item from pq if we get a larger val, or if it's
        index is outside of permissible values for the window.

        Can't use a stack, as let's say existing stack vals are [3,1]
        and we want to add a 2. We will need to remove the 1 without removing
        the 3, and make stack as [3,2], which is not permissible.
        '''
        pq = []
        heapq.heapify(pq)
        l=0
        ans = []

        for r in range(len(nums)):
            curr = (-nums[r],-r) #curr[0] = -val, curr[1] = -ix
            while len(pq) and (-pq[0][0] <= nums[r] or -pq[0][1] < l):
                heapq.heappop(pq)
            heapq.heappush(pq, curr)

            if r-l+1 < k:
                continue #not gotten a full window yet
            
            ans.append(-pq[0][0])
            l += 1
        
        return ans