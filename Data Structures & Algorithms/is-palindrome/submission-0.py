class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif (s[l].lower() != s[r].lower()):
                return False
            else:
                l += 1
                r -= 1
        
        return True