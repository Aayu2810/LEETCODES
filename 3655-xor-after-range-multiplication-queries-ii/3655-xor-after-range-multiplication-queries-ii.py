MOD = 1_000_000_007
MAXN = 100_000
BLOCK = 200

inv = [1] * (MAXN + 1)
for v in range(2, MAXN + 1):
    inv[v] = MOD - (MOD // v) * inv[MOD % v] % MOD

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        events = []

        for l, r, k, v in queries:
            if v == 1:
                continue
            elif (r - l + 1) < BLOCK or k > BLOCK:
                for idx in range(l, r + 1, k):
                    nums[idx] = nums[idx] * v % MOD
            else:
                res = l % k
                events.append((k, res, (l - res) // k, v))
                if (st := (r - res) // k + 1) <= (n - 1 - res) // k:
                    events.append((k, res, st, inv[v]))

        if not events:
            return reduce(xor, nums)

        grouped = defaultdict(lambda: defaultdict(list))
        for k, res, st, v in sorted(events):
            grouped[k][res].append((st, v))

        for k, group in grouped.items():
            for res, evs in group.items():
                mul, e, stride = 1, 0, 0
                for i in range(res, n, k):
                    while e < len(evs) and evs[e][0] == stride:
                        mul = mul * evs[e][1] % MOD
                        e += 1
                    nums[i] = nums[i] * mul % MOD
                    stride += 1

        return reduce(xor, nums)