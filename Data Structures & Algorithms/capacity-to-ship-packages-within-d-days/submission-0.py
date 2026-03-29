def time_taken(weights, capacity):
    t = 0
    cur_cap = 0
    for w in weights:
        if w > cur_cap: #this weight has to wait till next day to be accomodated
            t += 1
            cur_cap = capacity
        cur_cap -= w
    return t

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        The capacity of the ship has to be atleast the maximum weight in weights (or else
        it won't be able to carry the heaviest package). On the other hand, we can decide
        that the upper bound is the sum of all the weights (i.e. carry all in 1 trip).
        From then onwards, carry out a binary search for the least weight capacity reqd
        such that total time is less than 'days'.
        Finding total time with a given weight capacity is O(n), so overall O(nlogn).
        This problem is very similar to #875. Koko Eating Bananas 
        '''
        l, r = max(weights), sum(weights)
        ans = r
        while l<=r:
            m = (l+r)//2
            t = time_taken(weights, m)
            if t <= days:
                ans = m
                r = m-1 #try to reduce the capacity required further
            else:
                l = m+1
        
        return ans