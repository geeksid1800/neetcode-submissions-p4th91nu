'''
Recursive Approach: Given a subproblem s[i:], how many characters would you need to exclude at
minimum, so all other characters are part of valid words?
Greedy approach will not work here. Consider a case where dict = [abc,bcdef] and s=abcdef
Greedily selecting a will lead to best possible soln of 3 excluded chars (def). Whereas if we
don't select a, ans will be 1 (selecting bcdef). So for each character, we have to evaluate if
including or excluding it would lead to a better outcome. 
'''
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        vocab = set(dictionary)
        cache = {len(s):0} #memoization
        def recur(i) -> int:
            if i == len(s): return 0
            if i in cache: return cache[i]

            res = 1 + recur(i+1) # if we exclude current character, add 1 
            for j in range(i,len(s)): #try to check if s[i:j] (inclusive) is a valid word
                curr = s[i:j+1]
                if curr in vocab:
                    res = min(res, recur(j+1))
                
            cache[i] = res
            return res

        return recur(0)