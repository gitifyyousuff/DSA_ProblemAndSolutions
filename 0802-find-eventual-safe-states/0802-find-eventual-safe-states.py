class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        #hashmap for safe 
        safe ={}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            safe[i] = True
            return True
            
        result = []  
        for i in range(n):
            if dfs(i):
                result.append(i)
                
        return result       
        
        
        