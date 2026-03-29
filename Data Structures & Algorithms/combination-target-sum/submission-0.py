'''
For each element, we have 2 choices:
1) Choose to subtract it from target and not move forward (as we may choose it again next time)
2) Not choose it, and thus move forward
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def recur(ix, curArr, target):
            if target == 0:
                ans.append(curArr)
                return
            if target < 0 or ix==len(nums):
                return
            
            recur(ix, curArr + [nums[ix]], target - nums[ix])
            recur(ix+1, curArr, target)
        
        recur(ix=0, curArr=[], target=target)
        return ans