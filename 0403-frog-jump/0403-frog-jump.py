class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        #Basic check
        if stones[1] !=1:
            return False
        
        #since 0th idx is guaranteed to be 0, starting from 1st idx and 1 unit initially
        queue = [(1,1)]
        last_stone = stones[-1]
        seen = set()
        #type cast to set to speed up the queue
        stones = set(stones)
        #BFS
        while queue:
            #where k is the distance between one stone to another stone
            stone_num,k = queue.pop(0)
            if stone_num == last_stone:
                return True
            for neighbour in [k-1,k,k+1]:
                #To get next_possible positions 
                next_pos = stone_num + neighbour
                #we should not travel backward (k-1) and to travel only forward
                if next_pos == stone_num:
                    continue
                    
                if next_pos in stones and (next_pos,neighbour) not in seen:
                    queue.append((next_pos,neighbour))
                    seen.add((next_pos,neighbour))
                    
        return False
                
            
        