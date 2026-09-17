class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = str(len(s))
            encoded += l + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j+=1
            num = int(s[i:j])
            decode.append(s[j+1:j+1 + num])
            i = j+1+num
        return decode


       
