class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # find the char freq of t, start off a small window for s, keep moving l and r until the first character in t exist, slowly expand the window to capture other chars
        # if the current char added to window is extra, consider moving l if char at l is the same char as r 

        # brute force, every index check for shortest to get same char freq as t

        charT = {}

        for i in range(len(t)):
            charT[t[i]] = charT.get(t[i], 0) + 1

        mem = {}
        l = 0
        bestL = 0
        bestR = 0
        length = 0

        for r in range(len(s)):
            if s[r] in charT:
                mem[s[r]] = mem.get(s[r], 0) + 1
                while not s[l] in charT or mem[s[l]] > charT[s[l]]: 
                    if s[l] in mem and mem[s[l]] > charT[s[l]]:
                        mem[s[l]] -= 1
                    l += 1
            passes = all(mem.get(key, 0) >= value for key, value in charT.items())
            if passes and length == 0:
                bestR = r
                bestL = l
                length = r - l + 1
            elif r - l + 1 < length and passes:
                bestR = r
                bestL = l
                length = r - l + 1

        if length != 0: 
            return "".join(s[bestL:bestR+1])
        else:
            return ""