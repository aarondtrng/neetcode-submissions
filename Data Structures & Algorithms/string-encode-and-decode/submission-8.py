class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = str(len(s))
            encoded += l + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        print(s+"\n")
        decode = []
        for i in range(len(s)):
            if s[i] == "#" and s[i+1] != "#":
                j = 1
                num = ""
                while s[i-j].isdigit():
                    num = s[i-j] + num
                    j += 1
                print(num)
                decode.append(s[i+1:i+int(num)+1])
        print(decode)
        return decode


       
