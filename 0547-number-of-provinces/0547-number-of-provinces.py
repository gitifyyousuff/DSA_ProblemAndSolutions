class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Union-Find algorithm
        par = [i for i in range(len(isConnected)+1)]
        rank = [0] * (len(isConnected)+1)
        
        def find(n):
            if n == par[n]:
                return n
            else:
                return find(par[n])
        
        #n1-node1,n2-node2 respectively
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1 == p2 :
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
                
            return True
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i,j)
        count = 0            
        for j in range(len(isConnected[0])):
            if find(j) == j:
                count += 1
        return count
            
        
     