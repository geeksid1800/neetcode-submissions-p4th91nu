'''
Simple recursive solution O(2^n) TC
At each point, you can make two choices, leading to two subsets:
1) Include the current element in the subset you've built so far
2) Don't include it
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recur(ix, arr):
            if ix == len(nums):
                ans.append(arr)
                return
            
            recur(ix+1, arr + [nums[ix]]) #create array out of single element nums[ix]
            recur(ix+1, arr)

        recur(0, [])
        return ans