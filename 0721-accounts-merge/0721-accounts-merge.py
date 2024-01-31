class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self,x):
        if x == self.par[x]:
            return x
        return self.find(self.par[x])
    
    def union(self,x1,x2):
        n1,n2 = self.find(x1),self.find(x2)
        
        if n1 == n2:
            return False
        
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
        elif self.rank[n1] < self.rank[n2]:
            self.par[n1] = n2
        else:
            self.par[n1] = n2
            self.rank[n1] += 1
         
        return True
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #instantiating UnionFind class
        uf = UnionFind(len(accounts))
        
        #hashmap for {email:idx}
        emailAcc = {} 
        
        # where i is index, a is complete account(name and email list)
        # e is emails since it's starting from index 1
        for i,a in enumerate(accounts):
            for e in a[1:]:
                #check both idx points to same email
                if e in emailAcc:
                    uf.union(i,emailAcc[e])
                else:
                    emailAcc[e] = i
                    
        #emailGrp hashmap ->{indx1:[email1,email2]...}
        emailGrp = defaultdict(list)
        
        for e,i in emailAcc.items():
            leader = uf.find(i)
            emailGrp[leader].append(e)
            
        #iterate emailGrp hashmap and prepare the result
        res = []
        for i,e in emailGrp.items():
            names = accounts[i][0]
            res.append([names] + sorted(emailGrp[i]))
                       
        return res
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        