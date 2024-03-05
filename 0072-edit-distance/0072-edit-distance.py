class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)+1
        n = len(word2)+1
        
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # filling up 0 to m,n range
                if i == 0:
                    dp[i][j] = j
                elif j ==0 :
                    dp[i][j] = i
                #getting diagonal top value    
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                #3 operations min val  + 1  
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1
                    
        return dp[-1][-1]