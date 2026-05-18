import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1 #0-indexing
            rem = columnNumber%26
            ans.append(chr(ord('A') + rem))
            columnNumber = columnNumber//26
        
        return "".join(reversed(ans))