class Solution:
    def minTimeToReach(self, move_time: List[List[int]]) -> int:
        curr = [0, 0]
        n = len(move_time)
        m = len(move_time[0])

        # Initialize distances array with infinity
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0  # Starting point time is 0
        
        # Priority queue for Dijkstra (time, x, y)
        # Using min-heap to always process the node with minimum time first
        pq = [(0, 0, 0)]  # (time, x, y)
        
        while pq:
            curr_time, x, y = heapq.heappop(pq)
            
            # Skip if we've already found a better path
            if curr_time > dist[y][x]:
                continue
            
            # Check if we've reached the destination
            if y == n - 1 and x == m - 1:
                return curr_time
            
            # Explore adjacent rooms
            adjacents = self.getAdjacent([x, y], move_time)
            for adj_x, adj_y in adjacents:
                # Calculate new time to reach adjacent cell
                new_time = max(curr_time, move_time[adj_y][adj_x]) + 1
                
                # Update if we found a better path
                if new_time < dist[adj_y][adj_x]:
                    dist[adj_y][adj_x] = new_time
                    heapq.heappush(pq, (new_time, adj_x, adj_y))
        
        return dist[n-1][m-1]

    def getAdjacent(self, curr: List[int], move_time: List[List[int]]) -> List[int]:
        r = len(move_time)
        c = len(move_time[0])
        
        x = curr[0]
        y = curr[1]

        adjacents = []

        if x != 0:
            adjacents.append([x - 1, y])
        if x != c - 1:
            adjacents.append([x + 1, y])
        if y != 0:
            adjacents.append([x, y - 1])
        if y != r - 1:
            adjacents.append([x, y + 1])

        return adjacents