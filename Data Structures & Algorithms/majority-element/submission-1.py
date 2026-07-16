'''
The true element's count should outnumber all other element's counts, as there's
atleast n/2 of it itself.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMaj, currentMaj = 1, nums[0]
        for num in nums[1:]:
            if num == currentMaj: countMaj += 1
            else:
                if countMaj == 1: currentMaj = num #change the majority elmt
                else: countMaj -= 1
        
        return currentMaj