class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        filtered = "".join(char.lower() for char in s if char.isalnum())
        last = len(filtered)-1

        while(first < last):
            if filtered[first] != filtered[last]:
                return False
            first+=1
            last-=1
        return True