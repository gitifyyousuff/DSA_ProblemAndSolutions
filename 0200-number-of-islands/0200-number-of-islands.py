class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS 
        #edge case
        if not grid:
            return 0
        
        islands = 0
        visit = set()
        
        #dimension of grid and iterating over
        ROWS,COLS = len(grid), len(grid[0])
        
        #helper function
        def bfs(r,c):
            #queue since BFS
            q= deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                #possible up,down,right,left directions
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                #dr - diff in row and dc- diff in col
                for dr,dc in directions:
                    r,c = row+dr,dc+col
                    #inbound check
                    if (r in range(ROWS) and c in range(COLS)
                    and grid[r][c] == "1" and 
                    (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
                    
        return islands