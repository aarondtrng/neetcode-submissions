class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()
        l = 0
        maxF = 0
        maxLen = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0

            freq[s[r]] += 1
            maxF = max(maxF,freq[s[r]])

            while((r-l+1) - maxF) > k:
                freq[s[l]] -= 1
                l+=1
            maxLen = max(maxLen,r-l+1)
        return maxLen
            