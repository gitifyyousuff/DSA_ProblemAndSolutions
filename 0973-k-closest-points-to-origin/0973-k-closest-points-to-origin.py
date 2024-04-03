class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #creating heap list
        min_heap = []

        
        #calculating the euclidian absolute distance but not 
        #taking the root since it is not required for this problem
        for x,y in points:
            dist = (x**2)+(y**2)
            min_heap.append([dist,x,y])
        
        #convert the list to heap
        heapq.heapify(min_heap)
      
        #pop out min distance on the heap  k times to find the k closest value
        res = []
        while k>0:
            dist,x,y = heapq.heappop(min_heap)
            res.append([x,y])
            k -=1

        return res
       