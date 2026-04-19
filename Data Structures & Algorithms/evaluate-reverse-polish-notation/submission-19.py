class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ("+", "-", "*", "/")
        for t in tokens:
            if t in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num1) / num2))
            else:
                stack.append(int(t))
        return stack[0]