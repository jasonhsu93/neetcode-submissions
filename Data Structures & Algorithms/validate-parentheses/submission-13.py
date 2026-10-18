class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) == 0: 
                return False
            elif char == ')':
                temp = stack.pop() 
                if temp != '(':
                    return False
            elif char == ']':
                temp = stack.pop() 
                if temp != '[':
                    return False
            elif char == '}':
                temp = stack.pop()
                if temp != '{':
                    return False

        if len(stack) != 0:
            return False

        return True
