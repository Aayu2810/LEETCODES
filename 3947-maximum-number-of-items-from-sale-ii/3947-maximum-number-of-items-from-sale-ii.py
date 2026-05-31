class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        vals = [x[0] for x in items]
        freq = Counter(vals)
        mx = max(vals)
        factor = {}
        for v in freq: 
            c = 0 
            m = v 
            while m <= mx: 
                if m in freq: c += freq[m]
                m += v 
            c -= 1 
            factor[v] = c 
        pre = []
        mn = float('inf')
        for i in range(n):
            v, cost = items[i]
            c = factor[v]
            pre.append([v, cost, c, cost/(2 if c > 0 else 1)])
            mn = min(mn, cost)
        pre.sort(key=lambda x:(x[3],-x[2]))
        res = budget//mn 
        cnt = 0 
        i = 1 
        for x, y, z, w in pre: 
            c = min(z, (budget // y))
            cnt += c*2
            budget -= c*y 
            res = max(res, cnt + (budget//mn))
        return res