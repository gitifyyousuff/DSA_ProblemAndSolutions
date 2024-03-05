class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        
        #setting cols of the dp array
        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
            
        #setting rows of the dp array
        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
            
       
        
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 1:
                    continue
                    
                dp[r][c] = dp[r][c-1]+dp[r-1][c]
                
        
        return dp[-1][-1]
        
        