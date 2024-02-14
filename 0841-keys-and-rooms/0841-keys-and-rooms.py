class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #n represents number of rooms
        n = len(rooms)
        visited = set()
        
        #r represents each room
        def dfs(r):
            visited.add(r)
            for room in rooms[r]:
                if room not in visited:
                    dfs(room)
                    
        dfs(0)
            
        return len(visited)== n