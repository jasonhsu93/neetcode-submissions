class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = []

        for s in strs:
            result.append(str(len(s)) + "!" + s)
       
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0

        while i < len(s):
            j = i + 1
            while j < len(s):
                if s[j] == '!':
                    break
                j += 1
            result.append(s[j+1:j+1+int(s[i:j])])
            i = j + 1 + int(s[i:j])

        return result


















































