'''
Standard Backtracking based problem. At each stage, given an index 'start', try to split 
s[start:] into valid words, if at all.
Do this by iterating j from start+1 to the end, and if s[start:j] (both inclusive) is a valid
word, then add it to the current solution, call recursively recur(j+1). At the end, to allow other
possibilities, remove the recent substring from curr. 
When start reaches beyond last index of s, you have found a valid solution.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        validWords = set(wordDict)
        ans = []
        curr = []

        def recur(start):
            #try seeing how s[start:] can be split into valid words, if at all it can
            if start == len(s):
                ans.append(" ".join(curr))
                return
            
            for j in range(start, len(s)): # s[start:j] inclusive is current substring
                if s[start:j+1] in validWords:
                    # print(f"Adding {s[start:j+1]}")
                    curr.append(s[start:j+1])
                    recur(j+1)
                    curr.pop()
        
        recur(0)
        return ans