from collections import deque
'''
It's obvious that when a senator gets a turn, they should remove the earliest
surviving member of other party. Eg [R,D,R,D], here ix 0 should remove ix 1 so
that ix 2 (R) will get a chance to vote, instead of removing ix 3.
When a senator gets their turn, they vote and move to the back of the process, so
it's natural to use a queue. Maintain a 'backlog' variable for how many of each
party have been scheduled for removal, so that when we get a senator of that party
comes in front, he is removed without a vote. Eg. ix 0 decides to remove ix 1, so
we increase backlog of 'D' to 1. When ix 1 comes to the front, we see D backlog is
1, so we pop him without casting his vote. We continue till one party has no
remaining senators.
'''
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        rem = [0]*2 #ix 0 represents R senators remaining, ix 1 for D senators
        for senator in senate:
            if senator=='R': rem[0] += 1
            else: rem[1] += 1
        backlog = [0]*2 #represents how many senators of this party have
        #been removed this turn already (so they won't get to vote)

        while rem[0] and rem[1]:
            x = 0 if q[0]=='R' else 1
            if backlog[x] == 0: #this senator can stil play, no opposition has removed him
                backlog[1-x] += 1
                rem[1-x] -= 1
                q.append(q[0]) #goes to the back for another turn
            else:
                backlog[x] -= 1 #he has been voted off, reduce backlog
            q.popleft()
        return 'Radiant' if rem[0]>0 else 'Dire'