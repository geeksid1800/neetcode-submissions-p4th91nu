class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for _ in range(26)]
        l = 0
        ans, maxF = 0,0
        for r, c in enumerate(s):
            freq[ord(c) - ord('A')] += 1
            maxF = max(maxF, freq[ord(c) - ord('A')])

            while (r-l+1) - maxF > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            ans = max(ans, (r-l+1))
        
        return ans