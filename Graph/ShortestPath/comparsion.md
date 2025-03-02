# Bellman-Ford vs Dijkstra's Algorithm

## Overview

Both **Bellman-Ford** and **Dijkstra's** algorithms are used for **single-source shortest path** problems, but they differ in approach, efficiency, and use cases.

## Comparison Table

| Feature                    | Bellman-Ford                                                                  | Dijkstra                                                               |
| -------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Graph Type**             | Works with graphs having negative weight edges                                | Works only with non-negative weight edges                              |
| **Time Complexity**        | \(O(VE)\)                                                                     | \(O((V+E) \log V)\) with a priority queue (Binary Heap)                |
| **Approach**               | **Dynamic Programming**: Iterates over all edges \(V-1\) times                | **Greedy**: Picks the shortest known distance at each step             |
| **Negative Weight Cycles** | Detects negative weight cycles                                                | Cannot handle negative weight edges                                    |
| **Optimal for**            | Graphs with negative weights or detecting negative cycles                     | Graphs with only non-negative weights, especially dense graphs         |
| **Updates Distance**       | Updates the distance iteratively for all edges                                | Updates distance greedily using a priority queue                       |
| **Data Structure Used**    | Simple edge list iteration                                                    | Priority queue (Min-Heap)                                              |
| **Best Used When**         | Graphs with negative weights or when we need to detect negative weight cycles | Graphs with non-negative weights, especially when optimized with heaps |

## When to Use

- **Use Bellman-Ford** when:

  - The graph **contains negative weight edges**.
  - You need to **detect negative weight cycles**.
  - The graph is relatively **small** or has **fewer edges** compared to vertices.

- **Use Dijkstra** when:
  - The graph has **only non-negative weights**.
  - You want a more **efficient** algorithm, especially for **dense graphs**.
  - You can utilize a **priority queue (Min-Heap) to optimize performance**.

## Example Implementations

### Bellman-Ford Algorithm (Python)

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains a negative weight cycle")
                return

        print("Vertex Distance from Source:", dist)
```

### Dijkstra's Algorithm (Python)

```python
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

## Conclusion

- Use **Bellman-Ford** if **negative weight edges or cycle detection** is required.
- Use **Dijkstra** if **efficiency** is the priority and the graph has **non-negative weights**.
- Both algorithms are crucial for different scenarios in graph-based problems.

---

🚀 Happy Coding!
