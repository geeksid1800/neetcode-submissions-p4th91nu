'''
We notice that a single change of sign in elements can dramatically change
the max subarr product. For example of [1,-2,-3,4], up until i=1, the max product
was from 1. However, at i=2 (-3), the max subarr prod actually came from -2*-3,
where -2 was the min subarr product until i=1. This is because of the -ve sign.
So we need to keep track of both the max and min subarr prod so far, as a
change in sign will flip which one of the 2 actually becomes useful.
In addition, at any point, we may choose to ignore the max and min and just start
a new subarr at that point. Eg [-1,8]. for i=1, max=min=-1, but better to just
take 8 as the max. so max is actually max(1,min,max)*nums[i]
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minYet, maxYet = 1,1
        ans = nums[0]
        for num in nums:
            minYet, maxYet = min(num,minYet*num,maxYet*num), max(num,minYet*num,maxYet*num)
            ans = max(ans, maxYet)
        
        return ans