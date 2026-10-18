class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = {}

        for i in range(len(s)): 
            countS[s[i]] = countS.get(s[i], 0) + 1

        countT = {}

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        if len(countT) != len(countS):
            return False

        for char, value in countS.items():
            if not char in countT:
                return False
            elif countT[char] != value:
                return False

        return True
