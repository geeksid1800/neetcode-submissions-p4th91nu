'''
Sliding Window+DP based solution.
Basically, for a given target index j, we can reach it from an index i 
if minJump<=j-i<=maxJump and both i and j are reachable.
Rearranging, we get for a given j, i needs to be in range [j-maxJump,j-minJump]
and s[i] == 0.
However, if we iterate along j, we realise we don't need to re-evaluate the
entire range for each j. Between curr-1 and curr, only 2 indices change in the
window, the very first one of the old window gets removed (i.e curr-1-maxJump),
and the last one of the new window gets added (ie curr-minJump).
So maintain a variable reachable, representing how many indices in the current
index's window can reach it. ie for curr how many elements in 
[curr-maxJump,curr-minJump] can themselves be reached.
Store past results in a dp[n] arr
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1': return False
        reachable = 0
        dp = [True] + [None]*(n-1) #index 0 is always guaranteed to be reachable

        for curr in range(1,n):
            remIx, addIx = curr-1-maxJump, curr-minJump #the old ix to be removed, and new one that is to be added
            if 0<=addIx<n and dp[addIx]: reachable += 1 #you can reach curr from addIx
            if 0<=remIx<n and dp[remIx]: reachable -= 1 #you used to be able to reach old curr from remIx

            dp[curr] = True if reachable>0 and s[curr]=='0' else False
        
        return dp[n-1]