'''
We will build the permutation layer-by-layer like an onion. First iter will return all permutations
of first 1 elements (ie only 1 permutation possible), and then save that.
Next iteration will take the previous list (perms), and add the second element in all possible
indices (0th to nth)to all existing permutations, and save all those permutations to perms,
overwriting perms. 
E.g. if nums = [1,2,3], after 1st iteration of outermost loop, perms = [[1]]
After 2nd iteration, perms will be overwritten by [[2,1], [1,2]]
After 3rd iteration, perms will be overwritten as `insert 3 in all possible indices for each list
in perms`: [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
First 3 are from adding '3' to various positions in [2,1], next 3 are adding 3 to [1,2]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(0,len(perm)+1):
                    perm_incr = perm.copy() #we will add 1 element to older perm in each iteration
                    perm_incr.insert(i, num) #inserts 'n' at index i of perm_copy
                    new_perms.append(perm_incr)
            perms = new_perms
            print(perms)

        return perms