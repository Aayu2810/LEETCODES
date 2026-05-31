class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        fr=Counter(str(n))
        co=0
        for i,v in fr.items():
            co+=int(i)*v
        return co