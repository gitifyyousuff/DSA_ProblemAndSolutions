class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] !=1:
            return False
        
        queue = [(1,1)]
        last_stone = stones[-1]
        seen = set()
        stones = set(stones)
        while queue:
            stone_num,k = queue.pop(0)
            
            if stone_num == last_stone:
                return True
            
            for neig in [k-1,k,k+1]:
                next_pos = stone_num + neig
                
                if next_pos == stone_num:
                    continue
                if next_pos in stones and (next_pos,neig) not in seen:
                    queue.append((next_pos,neig))
                    seen.add(((next_pos,neig)))
                     
        return False