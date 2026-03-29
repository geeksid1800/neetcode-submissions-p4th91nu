class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = dict() #mapping of counter to words
        
        for word in strs:
            c = [0] * 26
            for ltr in word:
                c[ord(ltr) - ord('a')] += 1
            c = tuple(c) #list is not hashable, but tuple is

            if c not in letters:
                letters[c] = [word]
            else:
                letters[c].append(word)
        ans = []
        for words_list in letters.values():
            ans.append(words_list)
        
        return ans
