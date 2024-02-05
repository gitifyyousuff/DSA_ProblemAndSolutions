class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #BFS approach
        row = len(mat)
        col = len(mat[0])
        
        q = deque()
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                else:
                    mat[r][c] = float("inf")
                    
        while q:
            r,c,dist = q.popleft()
            
            for dr,dc in directions:
                n_row,n_col = r+dr,c+dc
                
                if n_row < 0 or n_col < 0 or n_row == row or n_col == col:
                    continue
                    
                if mat[n_row][n_col] > dist +1:
                    mat[n_row][n_col] = dist+1
                    q.append((n_row,n_col,dist+1))
                    
        return mat
            
                    
                
        