class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans = 0
        start = 0 #stores the start of the current substring
        for ix, c in enumerate(s):
            print(m)
            if c in m:
                r = m[c] #remove until this index
                while start <= r:
                    #new substring starts from m[c]+1
                    m.pop(s[start], None)
                    start += 1
            
            m[c] = ix
            #curr substring is [start,ix] (inclusive)
            ans = max(ans, ix-start+1)
        
        return ans