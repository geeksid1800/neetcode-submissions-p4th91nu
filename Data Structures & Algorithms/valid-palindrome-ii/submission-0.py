def recur(s: str, l: int, r: int, rem: int):
    #rem is the number of letters that can still be removed (here rem= 0 or 1)
    while l<r:
        if s[l] == s[r]:
            return recur(s,l+1,r-1, rem)
        else:
            if rem:
                return recur(s,l+1,r, rem-1) or recur(s, l, r-1, rem-1)
            else:
                return False
    
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        return recur(s,0,len(s)-1,1)
