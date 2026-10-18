class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mem = set()
        l = 0
        max_sub = 0

        for r in range(len(s)):
            while s[r] in mem:
                mem.remove(s[l])
                l += 1
            mem.add(s[r])
            max_sub = max(max_sub, len(mem))

        return max_sub 
