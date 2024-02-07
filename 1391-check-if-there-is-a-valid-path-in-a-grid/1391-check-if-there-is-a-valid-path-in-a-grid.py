class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        #getting the dimensions
        rows,cols = len(grid),len(grid[0])

        #making all possible directions on each street
        up = {x:set([2,3,4]) for x in [2,5,6]}
        down = {x:set([2,5,6]) for x in [2,3,4]}
        left = {x:set([1,4,6]) for x in [1,3,5]}
        right = {x:set([1,3,5]) for x in [1,4,6]}

        q = deque([(0,0)]) #row,col

        grid[0][0] = -grid[0][0]

        directions = [[1,0,down],[0,1,right],[-1,0,up],[0,-1,left]]

        while q:
            r,c = q.popleft()

            # if r<0 or c<0 or r==rows or c==cols:
            #     continue

            if r == rows-1 and c == cols-1:
                return True

            for dr,dc,d in [[r+1,c,down],[r,c+1,right],[r-1,c,up],[r,c-1,left]]:
                if 0<=dr<rows and 0<=dc<cols and -grid[r][c] in d and grid[dr][dc] in d[-grid[r][c]]:
                    grid[dr][dc] = -grid[dr][dc]
                    q.append((dr,dc))

        return False   
                                    