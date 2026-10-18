class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestStr = ""

        for i in range(len(s)):
            # check for odd palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longestStr):
                    longestStr = s[l:r+1]
                r += 1
                l -= 1

            # check for even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longestStr):
                    longestStr = s[l:r+1]
                r += 1
                l -= 1

        return longestStr