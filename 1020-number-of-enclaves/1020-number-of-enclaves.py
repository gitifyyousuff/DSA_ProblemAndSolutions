class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #dfs algo
        #count the total number of 1's mean land
        #count the border 1's with dfs call 
        # total- border-dfs --> will give the result
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r,c):
            #Base condition
            if r < 0 or c < 0 or r == m or c == n or (r,c) in visited or grid[r][c] == 0:
                return 0
            res = 1
            visited.add((r,c))
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                res += dfs(nr,nc)
            return res
        
        
        total_land = 0 
        border = 0
        visited = set()
        for r in range(m):
            for c in range(n):
                total_land += grid[r][c]
                #call dfs only if it is land,border and not visited already
                if (grid[r][c] == 1) and ((r,c) not in visited) and (r in [0,m-1] or c in [0,n-1]):
                    border += dfs(r,c)
                
                
        return total_land - border
                
                    
                
        