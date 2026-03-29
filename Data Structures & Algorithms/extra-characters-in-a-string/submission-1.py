'''
Trie Approach: Try to solve and find the answer for a subproblem s[i:].
Initially add the entire vocabulary to a Trie.
Search approach remains more or less the same as recursive approach, except instead of 
looking in a hashset for s[i:j], you look in the Trie.
'''
class Trie:
    def __init__(self):
        self.root = dict()
    def insert(self, word) -> None:
        curr = self.root
        for c in word:
            curr[c] = curr.get(c, dict())
            curr = curr[c]
        curr['0'] = True
    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True if '0' in curr else False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary: trie.insert(word)

        cache = {len(s):0} #memoization
        def recur(i) -> int:
            if i == len(s): return 0
            if i in cache: return cache[i]

            res = 1 + recur(i+1) # if we exclude current character, add 1 
            for j in range(i,len(s)): #try to check if s[i:j] (inclusive) is a valid word
                curr = s[i:j+1]
                if trie.search(curr):
                    res = min(res, recur(j+1))
                
            cache[i] = res
            return res

        return recur(0)