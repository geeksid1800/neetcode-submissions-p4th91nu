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