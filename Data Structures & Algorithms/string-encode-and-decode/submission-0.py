class Solution:
    def encode(self, strs: List[str]) -> str:
        results = ""
        for s in strs:
            results += str(len(s)) + "@" + s
        
        return results

    def decode(self, s: str) -> List[str]:
        decoded_words = []
        i = 0

        while i < len(s):
            j = s.index("@", i)
            length = int(s[i:j])
            decoded_words.append(s[j+1: j+1+length])
            i = j + 1 + length
        
        return decoded_words

