def segmentCost(s: str, l: int, m: int, factors: list) -> int:
    best = m
    for d in factors[m]:
        groups = m // d
        changes = 0
        for offset in range(d):
            for t in range(
                groups // 2
            ): 
                if (
                    s[l + offset + t * d]
                    != s[l + offset + (groups - 1 - t) * d]
                ):
                    changes += 1
        best = min(best, changes)
    return best


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = [[] for _ in range(n + 1)]
        for d in range(1, n // 2 + 1):
            for m in range(d * 2, n + 1, d):
                factors[m].append(d)
        cost = [[0] * n for _ in range(n)]
        for l in range(n - 1):
            for r in range(
                l + 1, n
            ):  
                cost[l][r] = segmentCost(s, l, r - l + 1, factors)

        @cache
        def solve(seg: int, start: int) -> int:
            if seg == 1:  
                return cost[start][n - 1]
            limit = (
                n - 1 - 2 * (seg - 1)
            ) 
            return min(
                cost[start][e] + solve(seg - 1, e + 1)
                for e in range(start + 1, limit + 1)
            )

        return solve(k, 0)