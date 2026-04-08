class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        try:
            for c in s: 
                if c in ['[','{','(']:
                    open.append(c)
                elif c == ']':
                    if open.pop() != '[':
                        return False
                elif c == '}':
                    if open.pop() != '{':
                        return False
                elif c == ')':
                    if open.pop() != '(':
                        return False
        except:
            return False

        return not open
            
            



        