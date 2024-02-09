class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #union-find Algorithm
        n =len(stones)
        par = [i for i in range(n)]
        rank = [0] * n
        
        #find function
        def find(i):
            if i == par[i]:
                return i
            else:
                return find(par[i])
            
        #union function
        def union(p1, p2):
            x1, x2 = find(p1), find(p2)

            if x1 == x2:
                return False

            if rank[x1] > rank[x2]:
                par[x2] = x1
            elif rank[x1] < rank[x2]:
                par[x1] = x2
            else:
                par[x1] = x2
                rank[x2] += 1  # Increment rank of x2
            return True
                
        
        #logic for this problem
        rows,cols ={},{}
        removed = 0 
        for i, (row,col) in enumerate(stones):
            if row in rows:
                removed += union(i,rows[row])
            else:
                rows[row] = i
                
            if col in cols:
                removed += union(i,cols[col])
            else:
                cols[col] = i
                
        return removed
                
            
        
        