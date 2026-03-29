from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        It is guaranteed that there are enough hours to eat all the piles, h>=len(piles).
        That means, worst case, if k = max(piles), we will be able to eat all the bananas in
        time. However, if h > len(piles), there may be a lower k for which we can finish all.
        Lower bound of k is obviously 1, higher bound is max(piles), now do binary search
        to check how long it will take to finish all piles with current k.
        Finding time taken to eat all piles for given k is O(n) operation, overall O(nlogn)
        '''
        l, r = 1, max(piles)
        ans = 1
        while l<=r:
            k = (l+r)//2
            t = sum([ceil(bananas/k) for bananas in piles]) #total time taken with given k
            if t<=h:
                ans = k
                r = k-1 #we can potentially look at lower rates of eating
            else:
                l = k+1
        
        return ans