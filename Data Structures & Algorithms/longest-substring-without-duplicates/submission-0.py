class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            temp = []
            r = i
            currLen = 0
            while r < len(s)-1 and s[r] not in temp:
                    temp.append(s[r])
                    currLen+=1
                    r+=1
            maxLen = max(currLen,maxLen)
        return maxLen
                
                    
