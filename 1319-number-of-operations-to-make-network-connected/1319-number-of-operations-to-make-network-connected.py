class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #edge case
        if n-1 > len(connections):
            return -1
        
#         #union-find algorithm
#         par = [i for i in range(len(connections)+1)]
#         rank = [0] * (len(connections)+1)
        
#         def find(n):
#             if n == par[n]:
#                 return n
#             else:
#                 return find(par[n])
        
#         #n1-node1,n2-node2 respectively
#         def union(n1,n2):
#             p1,p2 = find(n1),find(n2)
            
#             if p1 == p2 :
#                 return False
            
#             if rank[p1] > rank[p2]:
#                 par[p2] = p1
#             elif rank[p1] < rank[p2]:
#                 par[p1] = p2
#             else:
#                 par[p1] = p2
#                 rank[p2] += 1
                
#             return True
        
#         #main logic
        
        
#         #finding extra_cable else connecting with n/w
#         extra_cable = 0
#         for x,y in connections:
#             if find(x) == find(y):
#                 extra_cable += 1
#             else:
#                 union(x,y)
                
#         #counting components and getting result
#         component = 0 
#         for i in range(n):
#             if par[i] == i:
#                 component += 1
                
#         return component-1

        #DFS
        graph = [set() for i in range(n)]
        visited = [False] *n
        
        #1. adjacency matrix
        for src,destn in connections:
            graph[src].add(destn)
            graph[destn].add(src)
            
        #2.DFS algo
        def dfs(node):
            #base case
            if visited[node]:
                return False
            
            visited[node] = True
            
            for neighbour in graph[node]:
                dfs(neighbour)
                
            return True
        
        #3. calculation
        return sum(dfs(node) for node in range(n))-1
                
        
                             
         
            
                
        

        
                
        
                
            
        
        
                
        
        