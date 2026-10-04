class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s): return res
        
        freqt = dict()
        freqs = dict()
        for c in t:
            freqt[c] = freqt.get(c,0)+1

        need = len(freqt)
        have = 0
        maxLen = float('inf')
        currLen = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r],0) + 1
            if s[r] in freqt and freqs[s[r]] == freqt[s[r]]:
                have+=1
            while have == need: 
                currLen = r-l+1
                if currLen < maxLen:
                    res = s[l:r+1]
                    maxLen = currLen
                freqs[s[l]] -= 1
                if s[l] in freqt and freqs[s[l]] < freqt[s[l]]:
                    have-=1
                l += 1
        return res
           
            

