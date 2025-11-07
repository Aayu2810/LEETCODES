class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()