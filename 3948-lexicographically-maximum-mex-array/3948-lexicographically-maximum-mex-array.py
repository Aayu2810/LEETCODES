from sortedcontainers import SortedSet

class Solution:
    def maximumMEX(self, a: List[int]) -> List[int]:
        n = len(a)
        sm = [0] * n
        
        # Suffix MEX precomputation
        s = SortedSet(range(n + 1))
        for i in range(n - 1, -1, -1):
            s.discard(a[i])
            sm[i] = s[0]
            
        ans = []
        st = SortedSet(range(sm[0] + 1))
        
        v = sm[0]
        for i in range(n):
            st.discard(a[i])
            
            # Safe dereference: if set is empty, all needed numbers are found
            p = st[0] if st else v 
            
            if p >= v:
                ans.append(p)
                st.clear()
                
                if i < n - 1:
                    v = sm[i + 1]
                    st.update(range(v + 1))
                    
        return ans