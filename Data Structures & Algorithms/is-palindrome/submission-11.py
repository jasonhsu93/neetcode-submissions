class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if (ord(string[left]) < ord('a') or ord(string[left]) > ord('z')) and (ord(string[left]) < ord('0') or ord(string[left]) > ord('9')):
                left += 1
            elif (ord(string[right]) < ord('a') or ord(string[right]) > ord('z')) and (ord(string[right]) < ord('0') or ord(string[right]) > ord('9')):
                right -= 1
            elif string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1

        return True