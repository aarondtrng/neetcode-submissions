class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        filtered = "".join(char.lower() for char in s if char.isalnum())
        if len(filtered) == 0:
            return False

        for last in range(len(filtered)-1,0,-1):
            if last == first:
                return True
            if filtered[first] != filtered[last]:
                print(last)
                print(first)
                return False
            first+=1
        return True