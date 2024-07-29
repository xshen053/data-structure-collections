# BFS

![BFS1](./imgs/bfs1.png)

# Template1 (need to record distance)
> Using lc 690. Employee Importance to explain the idea

```Python
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # graph representation 3: adjancency list
        graph = defaultdict(list)
        for e in employees:
            graph[e.id] = e

        total_importance = 0
        queue = collections.deque()
        queue.append(graph[id])
        # queue
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_e = queue.popleft()
                total_importance += cur_e.importance
                for sub_id in cur_e.subordinates:
                    queue.append(graph[sub_id])
        
        return total_importance
```

# Template2 (need to record distance)
> Using lc 787. Cheapest Flights Within K Stops
to explain the idea

```Python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cheapest price so far
        dist = [float('inf')] * (n + 1)
        dist[src] = 0
        # level at most be k + 1
        level = 0
        
        # graph representation: using adj list
        graph = defaultdict(list)
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        queue = collections.deque()
        queue.append((src, 0))
        # queue with the shortest distance
        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                cur_city, cur_dist = queue.popleft()
                # iterate through all dst cities of current src cities
                for (dst_city, price) in graph[cur_city]:
                    # if distance is smaller, update it
                    if cur_dist + price < dist[dst_city]:
                        dist[dst_city] = cur_dist + price
                        queue.append((dst_city, cur_dist + price))
            if level == k + 1:
                break
        
        return dist[dst] if dist[dst] != float('inf') else -1
        
```
