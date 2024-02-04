class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #BFS approach
        #if it reaches the destination via clear path, by default
        #it guarantees the shortest path.
        
        n = len(grid)
        #edge case
        if grid[0][0] !=0 or grid[n-1][n-1] !=0:
            return -1
        
       
        q = deque([(0,0,1)]) #row,col,length
        visited = {(0,0)}
        #all possible 8 directions
        #first 4 entries denotes top,down,left and right
        #next 4 entries denotes diagonal left down & up, diagonal right down & up
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        
        while q:
            r,c,length = q.popleft()
            #check the inbound condition
            if r<0 or c<0 or r == n or c == n or grid[r][c] == 1:
                continue
            
            #means we have the destn with clear path
            if r == n-1 and c == n-1:
                return length
            
            #exploring all directions but not visiting the same cell
            for dr,dc in directions:
                n_row,n_col = r+dr,c+dc #neighbour row and neighbour col
                if (n_row,n_col) not in visited:
                    q.append((n_row,n_col,length+1))
                    visited.add((n_row,n_col))
        
        return -1
        
        
        
        