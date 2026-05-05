'''
Maintain the count of unmatched opening parenthesis, or the difference between # of ( and ).
Since * can be (,'',) it can sway the number by two depending on what it's interpreted as.
Hence, maintain a range of the min and max value of unmatched '('.
Anytime there is an unmatched right bracket, it is an automatic invalidation of string. So, if
even the most optimistic interpretation (i.e. leftMax) < 0 unmatched opening bracket, then
immediately return False. Also, if leftMax >=0 but there are some invalid interpretations so that
leftMin<0<=leftMax, prune the invalid interpretations by continuing with leftMin=0.
In the end return if we can find a valid interpretation of the string (i.e. its possible to get
unmatched '(' as 0).
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for sym in s:
            if sym == '(':
                leftMin,leftMax = leftMin + 1, leftMax + 1
            elif sym == '*':
                leftMin,leftMax = leftMin - 1, leftMax + 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax - 1
            if leftMax < 0:
                return False
            leftMin = max(0,leftMin)

        return leftMin<=0<=leftMax