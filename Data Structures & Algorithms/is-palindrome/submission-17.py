class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if (ord(string[i]) < ord('a') or ord(string[i]) > ord('z')) and (ord(string[i]) < ord('0') or ord(string[i]) > ord('9')):
                i += 1
            elif (ord(string[j]) < ord('a') or ord(string[j]) > ord('z')) and (ord(string[j]) < ord('0') or ord(string[j]) > ord('9')):
                j -= 1
            elif string[i] != string[j]:
                return False
            else:
                i += 1
                j -= 1

        return True