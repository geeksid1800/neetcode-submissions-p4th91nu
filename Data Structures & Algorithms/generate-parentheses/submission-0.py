def recur(tot, openP, ans, curr):
    if tot == 0:
        # reached total number of open Parantheses needed
        if openP == 0:
            ans.append(curr)
        return
    
    #we will always add an opening bracket, choice is how many to close at this stage
    curr += "(" #only adding the opening bracket
    openP += 1
    tot -= 1

    for i in range(openP+1):
        # choose how many of open brackets to close
        recur(tot, openP - i, ans, curr + ")"*i)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = ""
        tot = n
        openP = 0
        recur(tot, openP, ans, curr)
        return ans
