class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        if m+n != len(s3):
            return False
        
        #Tabulation dp technique used 
        #(n+1) and (m+1), +1 because to capture out of bound on either str
        dp = [[False]*(n+1) for _ in range(m+1)]
        #last[col][row] should be to drive the respective other [i][j] bool val
        dp[m][n] = True
        
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i<m and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j<n and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                    
        return dp[0][0]
        
        
        