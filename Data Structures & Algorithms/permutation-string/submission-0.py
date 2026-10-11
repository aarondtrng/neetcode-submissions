class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        maxCount = 0
        l = 0
        for r in range(len(s2)):
            count = 0
            if s2[r] in s1:
                if count == 0:
                    l = r
                while(s2[l] in s1):
                    count +=1
                    l+=1
            maxCount = max(maxCount, count)
        return maxCount == len(s1)
            