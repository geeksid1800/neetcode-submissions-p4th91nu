class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, resLen = s[0],1

        for i in range(n):
            #check how big of an odd-sized plndrom you can make with i as centre
            l,r = i,i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res, resLen = s[l:r+1], (r-l+1)
                l-=1; r+=1
            
            #check how big an even-sized pdrom you can make with i,i+1 as centre
            l,r = i, i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res, resLen = s[l:r+1], (r-l+1)
                l-=1; r+=1
        
        return res