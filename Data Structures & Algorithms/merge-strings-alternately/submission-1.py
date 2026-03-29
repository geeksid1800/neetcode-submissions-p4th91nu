class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        p = 0
        while p<len(word1) and p<len(word2):
            ans.extend([word1[p], word2[p]])
            p+=1
        ans.extend(word1[p:len(word1)])
        ans.extend(word2[p:len(word2)])
        return "".join(ans)