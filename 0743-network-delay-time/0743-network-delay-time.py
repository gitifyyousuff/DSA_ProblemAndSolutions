class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        
        #{src_node : [dest_node,weight]}
        for u,v,w in times:
            edges[u].append((v,w))
        
        #[(weight,node)]
        minheap = [(0,k)]
        
        #visited note should be striked off
        visit = set()
        
        #result
        t = 0
        
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)
            #BFS
            #neighbour node and weight
            #add to minheap [(weight1+weight2,node2)]
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1+w2,n2))
                    
        return t if len(visit)==n else -1
            
            
        
        