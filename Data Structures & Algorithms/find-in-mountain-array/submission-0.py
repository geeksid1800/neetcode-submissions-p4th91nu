# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        '''
        1) find mountain peak (at ix p) -> first element where arr[i+1] < arr[i]
        2) check for element in [0,p]
        3) check for element in [p+1,n-1]
        '''
        n = mountainArr.length()
        l,r = 0, n-1
        p = n-1
        while l<=r:
            m = (l+r)//2
            if (m+1<n) and (mountainArr.get(m) > mountainArr.get(m+1)):
                p = m
                r = m-1
            else:
                l = m+1

        # [0,p] is an increasing array, check here for target
        l,r = 0,p
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m+1
            else:
                r = m-1
        
        #[p,n-1] is a decreasing array, check here for target
        l, r = p, n-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                r = m-1
            else:
                l = m+1
        
        return -1