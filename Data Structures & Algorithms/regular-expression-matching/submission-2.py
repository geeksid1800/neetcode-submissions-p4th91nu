'''
Standard 2D DP/DFS based solution, match the corresponding chars in s and p.
Note: Watch the base conditions of the recursion and note I didn't add the case
for when string is empty but pattern is left as an automatic False. This is bec
cases like p="abc*" should match with s="ab", as when we get to c*, string is alr
empty, but the pattern can still evaluate to empty as well.
Due to this, we need to be careful to check if i1<n1 at all places where we're
accessing s[i1], as in a case like s=ab and p=.*c, it should evaluate to False.
The recursion paths for sequence c* where c is any char can be:
c* evaluates to "", ie we move forward 2 steps in p without moving forward in s
c* evaluates to "c", ie both c* in p and a single char in s are consumed
c* evaluates to c{2,}, ie. the next char in s is consumed but c* still remains.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[None]*(n2+1) for _ in range(n1+1)]

        def recur(i1, i2):
            if i1==n1 and i2==n2: return True
            if i2==n2 and not i1==n1: return False #pattern over, string left
            if dp[i1][i2] is not None: return dp[i1][i2]

            curr_char_matched = i1<n1 and p[i2] in ('.',s[i1])
            
            if i2<n2-1 and p[i2+1] == '*':
                # a sequence c* can mean 0 c, 1 c or more than 1 c
                #the first OR means c* got consumed w/o matching anything in s
                #the second means c* got consumed matching 1 char in s
                #third means c* matched 1 char in s but still remains not consumed
                dp[i1][i2] = (
                    recur(i1,i2+2) or
                    (curr_char_matched and recur(i1+1,i2+2)) or
                    (curr_char_matched and recur(i1+1,i2))
                )

            else:
                dp[i1][i2] = curr_char_matched and recur(i1+1,i2+1)
            
            return dp[i1][i2]
        
        return recur(0,0)