'''
Keep tracking the signs between nums. If they keep alternating, your subarr
will increase in length. 
If you encounter an '=', it's immediately broken,
and if you encounter a repeated sign, a new sequence starts from that point.
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        curr,ans = 1,1
        prevSign = None
        for i in range(1,n):
            if arr[i] > arr[i-1]: currSign = 'g'
            elif arr[i] < arr[i-1]: currSign = 'l'
            else: currSign = 'e'

            if currSign == 'e':
                curr = 1 #end the sequence immediately.
            elif prevSign in ('g','l') and currSign==prevSign:
                #start of a new sequence with this and prev being the first ones
                curr = 2
            else:
                curr += 1
            ans = max(ans,curr)
            prevSign = currSign
        
        return ans