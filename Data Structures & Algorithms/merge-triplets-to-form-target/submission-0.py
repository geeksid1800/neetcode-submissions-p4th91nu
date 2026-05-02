'''
Since we are always doing max() of two triplets to reach target, we know that atl.
1 triplet must have in the same position the same value as target. E.g. if target=
[7,6,5], then atleast one triplet must have triplet[0] as 7. Also, for that triplet
to be a part of the answer, it must have it's other cols smaller than the 
corresponding values in target, i.e. the triplet(s) with triplet[0] as 7 must have
triplet[1]<=6 and triplet[2]<=5, or else target can't be formed with it.
So we subtract target from each triplet and see for each of the 3 cols, we can
find atleast one triplet where the triplet[col]==0 and all other cols <= 0.
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        for i,triplet in enumerate(triplets):
            triplets[i] = [x-t for x,t in zip(triplet,target)]

        found = 0
        '''now look columnwise to make sure the reqd value is there somewhere,
        and if it is there, that none of its other elements in the triplet are
        too large to form target.'''
        for col in range(3):
            for triplet in triplets:
                if triplet[col]==0 and all(x<=0 for x in triplet):
                    found += 1
                    break
        
        return True if found==3 else False            