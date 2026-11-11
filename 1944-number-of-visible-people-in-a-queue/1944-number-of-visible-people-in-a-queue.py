# Python
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        st = []

        for i in range(len(heights) - 1, -1, -1):
            if not st:
                st.append(heights[i])
                ans.append(0)
            else:
                count = 0

                while st and st[-1] <= heights[i]:
                    st.pop()
                    count += 1

                if st:
                    count += 1

                st.append(heights[i])
                ans.append(count)

        return ans[::-1]