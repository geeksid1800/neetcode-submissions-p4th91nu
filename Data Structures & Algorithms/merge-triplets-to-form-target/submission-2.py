'''
Approach #2: Since we are doing max() on triplets to get target, ANY triplet with
any value greater than target is immediately discarded. Check the remaining triplets
to see if atleast 1 has a value exactly equal to that in target
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        found = set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue #this is not a useful triplet

            for ix,val in enumerate(t): #check if any col in t matches that in tgt
                if val == target[ix]: found.add(ix)

        return len(found) == 3 