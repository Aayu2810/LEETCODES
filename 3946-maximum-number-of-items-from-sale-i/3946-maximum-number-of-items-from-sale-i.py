class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        maxi=0
        mini=float('inf')
        for i in items:
            maxi=maxi if maxi>i[0] else i[0]
            mini=mini if mini<i[1] else i[1]
        count=[0]*(maxi+1)
        for i in items:
            count[i[0]]+=1
        val=[0]*n
        for i in range(n):
            f=items[i][0]
            total=0
            for j in range(f,maxi+1,f):
                total+=count[j]
            val[i]=total
        dp=[-1]*(budget+1)
        dp[0]=0
        for i in range(n):
            cost=items[i][1]
            value=val[i]
            for j in range(budget,cost-1,-1):
                if dp[j-cost]!=-1:
                    dp[j]=max(dp[j],dp[j-cost]+value)
        maxtotal=0
        for i in range(budget+1):
            if dp[i]!=-1:
                extra=(budget-i)//mini
                maxtotal=max(maxtotal,dp[i]+extra)
        return maxtotal