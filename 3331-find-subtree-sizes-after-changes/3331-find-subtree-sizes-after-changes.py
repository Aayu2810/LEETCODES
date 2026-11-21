class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        children = [[] for _ in s]
        for x in range(1, len(s)):
            children[parent[x]].append(x)
        size, last = [1] * len(s), {}  # last[c]: the deepest node with letter c on the path from the root

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)  # the closest ancestor with the same letter, or -1
            last[c] = x
            for child in children[x]:
                dfs(child)
            last[c] = above
            if x:  # the root has no parent
                size[above if above >= 0 else parent[x]] += size[x]

        dfs(0)
        return size