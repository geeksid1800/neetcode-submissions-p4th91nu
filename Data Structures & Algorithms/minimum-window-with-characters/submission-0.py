class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        sCount = {}
        l = 0
        matches = 52
        res = "1" + s

        for c in t: tCount[c] = tCount.get(c,0) + 1
        
        #check how many non-zero counts in tCount
        matches -= len(tCount.keys())
        
        #increase the window until we have all character of t within,
        #then try to decrease to minimise size
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r],0) + 1
            if sCount[s[r]] == tCount.get(s[r],0):
                matches += 1

            while (matches == 52) and (l<=r):
                if (r-l+1) < len(res):
                    res = s[l:r+1]
                sCount[s[l]] -= 1
                if sCount[s[l]] == tCount.get(s[l],0) - 1:
                    matches -= 1
                l += 1
        
        return "" if (res[0] == "1") else res


                
