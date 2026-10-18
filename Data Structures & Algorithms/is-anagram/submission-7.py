class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        memS = {}
        memT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in memS:
                memS[s[i]] += 1
            else:
                memS[s[i]] = 1
            
            if t[i] in memT:
                memT[t[i]] += 1
            else:
                memT[t[i]] = 1
        
        for char,count in memS.items(): 
            if char not in memT.keys():
                return False
            else:
                if count != memT[char]:
                    return False
            
        return True