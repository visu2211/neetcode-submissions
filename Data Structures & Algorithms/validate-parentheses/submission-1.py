class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        o = ('(', '[', '{')
        for c in s:
            if c in o:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if dic[c] != stack.pop():
                    return False
        return len(stack) == 0