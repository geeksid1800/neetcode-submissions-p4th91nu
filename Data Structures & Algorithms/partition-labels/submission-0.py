'''
Since all instances of a letter need to be in the same substring, it means any time
we encounter a letter, we have to make sure to extend the substring until ATLEAST
the last occurence of the letter. This will further spawn more letters that are in
between the first occurence of our current letter, and the last, so we need to make
sure we need to stretch our substring to reach until the last occurence of all of
them.
We also know that if we reach the last occurence of a letter in s, we should
immediately end the current substring there and start a new one going forwards,
in order to maximise # substrings.
So for the current substring, we maintain the last occurence of any letter within
it so far, and update it as we keep finding new letters while traversing s.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [None]*26
        for ix,c in enumerate(s):
            last[ord(c) - ord('a')] = ix
        
        ans = []
        currLast, currCount = 0,0
        for ix,c in enumerate(s):
            currLast = max(currLast, last[ord(c)-ord("a")])
            currCount += 1 #size of current substring
            if currLast == ix: #we reached the last occurence of all the letters
                #that appear in our substring
                ans.append(currCount)
                currCount = 0
        
        return ans