class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return []

        encoded_string = " ".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        decoded_strs = s.split(" ")
        return decoded_strs
