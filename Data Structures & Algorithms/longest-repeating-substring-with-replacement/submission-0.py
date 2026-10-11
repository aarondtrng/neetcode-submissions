class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] +=1
        print(freq)

        return max(freq.values())+k