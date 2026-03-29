class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        counts1, counts2 = [0]*26, [0]*26
        matches = 0 #stores how many letters in s1 and current window of s2
        # have the same counts. If we get matches==26, we have a permutation. 

        for i in range(n):
            # fill up counts of first window of s2 as well as entire s1
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1

        #one time full load of counts
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        l = 0
        for r in range(n,len(s2)):
            if matches == 26:
                print(s2[l:l+n])
                return True
            #remove l from counts2, and at max the value of matches changes by 1
            ix = ord(s2[l]) - ord('a')
            counts2[ix] -= 1
            if counts1[ix] == counts2[ix]: matches += 1
            elif counts1[ix] == counts2[ix] + 1:
                #earlier they were equal, now counts2[ix] is 1 less 
                matches -= 1
            l += 1

            #add r to counts2, and at max the val of matches changes by 1
            ix = ord(s2[r]) - ord('a')
            counts2[ix] += 1
            if counts1[ix] == counts2[ix]: matches += 1
            elif counts1[ix] == counts2[ix] - 1:
                #earlier they were equal, now counts2[ix] has increased by 1
                matches -= 1
        
        #might be the case that after adding the last char in s2 as r,
        #matches becomes 26, i.e. the last window of s2 is a perm. of s1
        return matches == 26