class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        #make a window of size k
        l,r = 0,k-1 #current window is [0,k-1]
        for r in range(k,n):
            # new candidate is r to replace l (ie shifting window by 1)
            if abs(arr[r] - x) < abs(arr[l] - x):
                #r has to be strictly closer than l to x
                #in case of equal distance, l is preferred. 
                l += 1
            else:
                break
        
        return arr[l:l+k]
        

