class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for letter in s:
            if letter not in sDict:
                sDict[letter] = 0
            sDict[letter] += 1
        
        tDict = {}
        for letter in t:
            if letter not in tDict:
                tDict[letter] = 0
            tDict[letter] += 1
        
        return sDict == tDict