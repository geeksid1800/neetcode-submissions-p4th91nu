'''
Keep tracking the signs between nums. If they keep alternating, your subarr
will increase in length. If you encounter an '=', it's immediately broken,
and if you encounter a repeated sign, a new sequence starts from that point.
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        signs = [None]*(n-1)
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                signs[i-1] = 'l'
            elif arr[i] > arr[i-1]:
                signs[i-1] = 'g'
            else: signs[i-1] = 'e'
        
        curr, ans = 0,0
        for i in range(len(signs)):
            #eg [5,4,6,6,2,4,2]  => [l,g,e,l,g,l] => ans = 4 (last 3 signs)
            if i==0:
                curr = 0 if signs[i] == 'e' else 1 
            elif signs[i] == 'e':
                curr = 0
            elif signs[i] == signs[i-1]:
                curr = 1
            else:
                curr += 1
            
            ans = max(ans,curr)
        
        return ans+1