class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in close_to_open:
                if not stack or stack.pop() != close_to_open[char]:
                    return False
            else:
                stack.append(char)
        return not stack