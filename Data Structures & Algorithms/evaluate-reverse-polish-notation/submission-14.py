class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = {"+", "-", "*", "/"}
        stack = []
        for i in tokens:
            if i in s:
                num2 = stack.pop()
                num1 = stack.pop()
                match i:
                    case "+":
                        stack.append((num1 + num2))
                    case "-":
                        stack.append((num1 - num2))
                    case "*":
                        stack.append((num1 * num2))
                    case "/":
                        stack.append(int(float(num1) / num2))
            else: stack.append(int(i))
        return stack[0]