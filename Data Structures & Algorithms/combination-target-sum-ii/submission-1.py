'''
Similar approach to Combination Sum I, but we may have duplicate values in nums, and we can choose
each element in nums only once, and return only unique combinations.
First, sort nums so all identical values are together.
So, if we choose the current element, we need to increment the ix by 1 in next recursive call.
But if we don't choose current ix, we have to skip past all identical values so we don't get
duplicate solutions
'''
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def recur(ix, curArr, target):
            if target == 0:
                ans.append(curArr)
                return
            if target < 0 or ix == len(nums) or nums[ix]>target:
                return
            
            recur(ix+1, curArr+[nums[ix]], target-nums[ix])
            # if we aren't picking nums[ix], we need to skip ahead past all identical values
            nxt = ix
            while nxt < len(nums) and nums[nxt]==nums[ix]: nxt += 1
            recur(nxt, curArr, target)
        
        recur(0, [], target)
        return ans