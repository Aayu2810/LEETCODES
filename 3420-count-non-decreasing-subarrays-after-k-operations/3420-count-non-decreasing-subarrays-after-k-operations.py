class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        operations = 0
        q = []
        cnt = [[] for _ in range(n)]
        pos = [n] * n
        st = []

        left = 0
        for right in range(n):
            while st and nums[right] >= nums[st[-1]]:
                pos[st[-1]] = right
                st.pop()
            if st:
                cnt[st[-1]].append(right)
            st.append(right)
            heapq.heappush(q, (-nums[right], right))
            operations += max(0, -q[0][0] - nums[right])
            while operations > k:
                for i in cnt[left]:
                    operations -= (nums[left] - nums[i]) * (
                        min(pos[i], right + 1) - i
                    )
                left += 1
            while q and q[0][1] < left:
                heapq.heappop(q)
            ans += right - left + 1

        return ans