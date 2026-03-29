'''
Similar to #78. Subsets.
Regardless of whether you choose i or not to be part of curr list, you have to advance i in next 
calls to recur(), because no repetition of elements.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def recur(i, curArr, k):
            if k==0:
                ans.append(curArr)
                return
            if i>n:
                return
            
            choseCurr = recur(i+1, curArr+[i],k-1)
            notChoseCurr = recur(i+1, curArr, k)
            return
        
        recur(1, [], k)
        return ans