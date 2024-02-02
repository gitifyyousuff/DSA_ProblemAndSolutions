class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board),len(board[0])
        
        def dfs(r,c):
            #Base case
            if (r<0 or c<0 or r==rows or c==cols or 
               board[r][c] !="O"):
                return
            #temporarily making as T
            board[r][c] = "T"
            #checking all possible directions
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)
            
        #1.checking all the borders and it's neighbour, then marking it as "T"
        #the unsurrounded region
        for r in range(rows):
            for c in range(cols):
                if (board[r][c]=="O" and
                  (r in [0,rows-1] or c in [0,cols-1])):
                    dfs(r,c)
        print(board)           
        #2.Checking if "O" and "T" cells, if "T" --> "O"
        #if already "O" ---> "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    
            
        