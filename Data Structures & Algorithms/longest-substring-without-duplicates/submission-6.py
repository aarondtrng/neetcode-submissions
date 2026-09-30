class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        temp = set()
    
        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1
            temp.add(s[r])
            maxLen = max(maxLen,r-l+1)    
        return maxLen
                
                    
