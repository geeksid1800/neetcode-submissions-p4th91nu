'''
Maintain 2 stacks, one for '(' and one for '*'. When you encounter a ), try to
match with ( if possible, and use a * otherwise. 
At the end of your string, if you have unmatched ( left in your stack,
see if you have remaining * in its stack that occur after the '('s to match them.
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStk,starStk = [],[]

        for ix,sym in enumerate(s):
            if sym == '(':
                leftStk.append(ix)
            elif sym == '*':
                starStk.append(ix)
            else:
                if not leftStk and not starStk: return False
                if leftStk: leftStk.pop()
                else: starStk.pop()
        
        while leftStk:
            if not starStk or leftStk[-1] > starStk[-1]: return False
            leftStk.pop()
            starStk.pop()

        return len(leftStk) == 0