class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #Floyd warshel Algorithm
        dist = [[float('inf')]*n for _ in range(n)]
        
        #making diagonal cell as 0
        for i in range(n):
            dist[i][i] = 0
                    
        #making direct connection weight marking for adjacency matrix 
        #s-source, d-destination, w-weight
        for s,d,w in edges:
            dist[s][d] = w
            dist[d][s] = w
            
        #making shortest possible distance on each edges to vertices 
        #mark it in adjacency matrix by floyd warshel formula
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    trans_dist = dist[i][k] + dist[k][j]
                    if dist[i][j] > trans_dist:
                        dist[i][j] = trans_dist
                        dist[j][i] = trans_dist
                        
                        
        #main logic
        min_city, min_reach = None,float('inf')
        for node_a in range(n):
            temp_reach = 0
            for node_b in range(n):
                if dist[node_a][node_b] <= distanceThreshold:
                    temp_reach += 1
            if temp_reach <= min_reach:  
                min_city = node_a
                min_reach = temp_reach
                
                
        
        return min_city
            
                    
                    
                    
                    
                    
                    
                    
                    
                    