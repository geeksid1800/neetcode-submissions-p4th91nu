'''
Similar logic to #40. Combination Sum II. Pre-sort nums before the recursion
If we choose nums[i], we can choose any future values with the same value as it.
However, if we didn't choose nums[i], we cannot choose any future indices with same value as it,
to prevent duplicate cases.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def recur(i, curArr):
            if i == len(nums):
                ans.append(curArr)
                return
            
            choseCur = recur(i+1, curArr + [nums[i]])
            #if we didn't choose nums[i] now, we must make sure we don't choose the same
            #value at any point in the future, to prevent duplicates.
            nxt = i
            while nxt<len(nums) and nums[nxt] == nums[i]: nxt += 1
            notChoseCur = recur(nxt, curArr)

        recur(0, [])
        return ans