class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s): return res
        
        freqt = dict()
        freqs = dict()
        for c in t:
            freqt[c] = freqt.get(c,0)+1

        maxLen = float('inf')
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r],0) + 1
            while freqt.items() <= freqs.items(): 
                print(res)
                freqs[s[l]] -= 1
                l+=1
                
                
        print(freqs) 
        print(freqt) 
        return res
           
            

