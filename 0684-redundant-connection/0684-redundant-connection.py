class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union-Find algorithm
        par = [i for i in range(len(edges)+1)]
        rank = [0] * (len(edges)+1)
        
        def find(n):
            if n == par[n]:
                return n
            else:
                return find(par[n])
#         def find(n):
#             p = par[n]
            
#             while p!=par[p]:
#                 par[p] = par[par[p]]
#                 p = par[p]
                
#             return p
        
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
                rank[p1] > rank[p2]
                
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
                
        