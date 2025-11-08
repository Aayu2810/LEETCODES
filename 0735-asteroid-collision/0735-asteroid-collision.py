class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            if a > 0 or not stack or stack[-1] < 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == -a:
                    stack.pop()
        return stack
        