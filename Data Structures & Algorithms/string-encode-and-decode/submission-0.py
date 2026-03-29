class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            buff=""
            while s[i] != '#':
                buff += s[i]
                i += 1
            #now s[i] == '#'
            word_len = int(buff)
            res.append(s[i+1:i+1+word_len])
            i = i+1+word_len
        return res