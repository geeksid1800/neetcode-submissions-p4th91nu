class Solution:
    def validPalindrome(self, s: str) -> bool:
        def recur(l,r,rem):
            if l>=r:
                return True
            if s[l] == s[r]:
                return recur(l+1,r-1,rem)
            #s[l] != s[r]: check if we can afford to remove one of l/r
            if rem>0:
                return recur(l+1,r,rem-1) or recur(l,r-1,rem-1)
            return False
        
        return recur(0,len(s)-1,1)