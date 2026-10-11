class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        while l < len(s):
            temp = []
            r = l
            currLen = 0
            while r < len(s) and s[r] not in temp:
                    temp.append(s[r])
                    currLen+=1
                    r+=1
            maxLen = max(currLen,maxLen)
            l=r
        return maxLen
                
                    
