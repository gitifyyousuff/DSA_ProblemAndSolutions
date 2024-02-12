class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #2 list to maintain trusted person and trustedTo person
        #a --> trustedTo , b -->trusted
        trustedTo = [0]* (n+1)
        trusted = [0]* (n+1)
        
        #let's increment list accordingly to check rule 1 and 2
        # Input: n = 3, trust = [[1,3],[2,3]] as example
        for a,b in trust:
            trustedTo[a] += 1
            trusted[b] += 1
            
        #end of the above step, both lists will become 
        #trustedTo ---> [0,1,1,0], trusted --->[0,0,0,2]
        #on the above step, it is clear the result is 3 since 3rd index satisfies
        for i in range(1,n+1):
            if trustedTo[i] == 0 and trusted[i] == n-1:
                return i
        return -1
            