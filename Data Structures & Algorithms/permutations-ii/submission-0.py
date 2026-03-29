from collections import Counter
'''
Instead of selecting elements by looping through nums like in #46.Permutations,
this case we will have a Counter for each unique value.
In each recursive dfs call, we will add a non-zero count element to currently constructed subarray,
decrement it's count, and recurse downwards.
When done with it, we will add back the element to the counter and continue with next element.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        ans, curr = [],[]

        def dfs(curr) -> None:
            if len(curr) == len(nums):
                ans.append(curr)
                return
            
            for num in c:
                if c[num] > 0:
                    c[num] -= 1
                    dfs(curr + [num])
                    c[num] += 1

        dfs(curr)
        return ans