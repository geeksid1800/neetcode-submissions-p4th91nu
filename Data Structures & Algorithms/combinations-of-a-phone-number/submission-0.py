class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'
        }
        ans = []
        def recur(ix, curr):
            if ix == len(digits):
                if curr:
                    ans.append("".join(curr))
                return
            candidates = mp.get(digits[ix],"")
            for char in candidates:
                recur(ix+1, curr+[char])
        
        recur(0,[])
        return ans