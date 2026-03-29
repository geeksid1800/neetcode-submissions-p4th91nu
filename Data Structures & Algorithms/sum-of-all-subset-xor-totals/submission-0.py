class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recur(i, total):
            if i == len(nums):
                return total
            
            choseCurr = recur(i+1, total ^ nums[i])
            notChoseCurr = recur(i+1, total)
            return choseCurr + notChoseCurr
        
    
        return recur(0, 0)