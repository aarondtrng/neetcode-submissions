class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        filtered = s.replace(" ","")

        for last in range(len(filtered)-1,0,-1):
            if not filtered[last].isalpha():
                continue
            if filtered[first].lower() != filtered[last].lower():
                # print(s[first] + str(first))
                # print(s[last] + str(last))
                return False
            first+=1
        return True