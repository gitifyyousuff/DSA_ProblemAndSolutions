class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #top-bottom approach
        #memoization
        cache = {}
        
        def dfs(i,j):
            #Base case 
            if j == len(t):
                return 1
            if i == len(s):
                return 0          
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
                
            return cache[(i,j)]
        
        return dfs(0,0)
            
            
        