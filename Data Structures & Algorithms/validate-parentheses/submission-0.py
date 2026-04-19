class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        signs = ["(", "{", "["]
        matching = {")" : "(", "}" : "{", "]" : "["}
        while index < len(s):
            if s[index] in signs:
                stack.append(s[index])
            else:
                if len(stack) > 0:
                    pop = stack.pop()
                else:
                    return False
                if matching[s[index]] != pop:
                    return False
            index += 1
        return len(stack) == 0