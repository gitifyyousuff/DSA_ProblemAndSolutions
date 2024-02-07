class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #BFS
        #0 -> unvisited, 1-> odd, -1 -> even
        seen = [0] * len(graph)
        
        def bfs(i):
            #seen[i] != 0 condition basically
            if seen[i]:
                return True
            
            q = deque([i])
            #marking even occurance as -1
            seen[i] = -1
            
            while q:
                i = q.popleft()
                
                #where n is the neighbour nodes of i'th node
                for n in graph[i]:
                    #adjacent node value check, (1,-1) check basically
                    if seen[i] == seen[n]:
                        return False
                    #seen[n] !=0, means not visited node
                    elif not seen[n]:
                        q.append(n)
                        seen[n] = -1 * seen[i]
            return True
                
        #checking each node in the graph if the bfs is not True 
        #for any of the node, then return False
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
        