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
            if s[i] == "#":
                l = int(s[i-1])+1
                decode.append(s[i+1:i+l])
        print(decode)
        return decode


       
