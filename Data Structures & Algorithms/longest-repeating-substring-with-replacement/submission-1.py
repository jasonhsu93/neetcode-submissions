class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # sliding window, left ptr starts at the left most, right ptr starts left most, slowly expand window while checking if window - max char freq <= k

        l = 0
        max_freq = 0
        result = 0
        charFreq = {}
        
        for r in range(len(s)):
            window = r - l + 1
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1
            max_freq = max(max_freq, charFreq[s[r]])

            while window - max_freq > k:
                charFreq[s[l]] -= 1
                l += 1
                window = r - l + 1
            
            result = window if window > result else result

        return result
        

