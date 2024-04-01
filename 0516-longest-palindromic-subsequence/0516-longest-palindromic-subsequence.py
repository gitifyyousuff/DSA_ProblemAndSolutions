class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #applying LCS(1143) here
        s2 = s[::-1]
        
        #bottom up approach
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s2)+1)]
        
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s[i] == s2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                    
        return dp[0][0]
        