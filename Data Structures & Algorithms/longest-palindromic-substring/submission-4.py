class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestStr = ""

        for i in range(len(s)):
            # odd 
            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > len(longestStr):
                    longestStr = s[l:r+1]
                l -= 1
                r += 1

            # even
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > len(longestStr):
                    longestStr = s[l:r+1]
                l -= 1
                r += 1

        return longestStr
                