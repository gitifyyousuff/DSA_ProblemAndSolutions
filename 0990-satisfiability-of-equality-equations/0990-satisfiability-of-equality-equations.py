class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        par = {chr(num): chr(num)for num in range(ord('a'),ord('z')+1)}
        
        def find(n):
            if n == par[n]:
                return n
            return find(par[n])
        
        for a,sign,_,b in equations:
            if sign == "=":
                par_x,par_y = find(a),find(b)
                par[par_x] = par_y
            
            
        for a,sign,_,b in equations:
            if sign == "!" and find(a) == find(b):
                return False
            
        return True
        