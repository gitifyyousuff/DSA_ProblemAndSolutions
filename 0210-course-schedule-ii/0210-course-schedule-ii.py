#Topological sort Algorithm----> only DAG (Directed Acyclic Graph) possible
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #To form adjacency list
        preAdj = {c:[] for c in range(numCourses)}
        for crs,preq in prerequisites:
            preAdj[crs].append(preq)
            
        print(preAdj)
            
        #unvisited - Not added visited set and result list
        #visiting - Added to cycle but not added to result list
        #visited - Added to ouput list
        result = []
        visited, cycle = set(),set()
        
        def dfs(cr):
            if cr in cycle:
                return False
            if cr in visited:
                return True
           
            
            cycle.add(cr)
            
            for pre in preAdj[cr]:
                if dfs(pre) == False:
                    return False
            cycle.remove(cr)
            visited.add(cr)
            result.append(cr)
            return True
           
        for cr in range(numCourses):
            #if it have cycle, then [] list will be returned
            if dfs(cr) == False:
                return []
            
        return result