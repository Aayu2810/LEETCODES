class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        lasta = -1
        firstb = n
        for i in range(n):
            if s[i] == "a":
                lasta = max(lasta, i)
            else:
                firstb = min(firstb, i)
        return lasta < firstb