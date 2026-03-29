class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = []
        first, last = strs[0], strs[-1]

        for c1,c2 in zip(first, last):
            if c1!=c2:
                break
            ans.append(c1)
        
        return "".join(ans)