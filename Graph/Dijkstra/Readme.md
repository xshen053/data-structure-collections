# Classic Dijkstra
> Use 743. Network Delay Time as an example to explain

```Python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # shortest cost from k to each node
        distTo = [float("inf")] * (n + 1)
        # since we don't need to know the path, so actually no need use edgeTo
        # edgeTo = [float("inf")] * (n + 1)
        # no node 0
        distTo[0] = 0

        # build graph representation: adj list
        #   - src: [(dst1, time1), (dst2, time2)]
        graph = defaultdict(list)
        for t in times:
            graph[t[0]].append((t[1], t[2]))

        distTo[k] = 0
        visited = set()
        pq = []
        heapq.heappush(pq, (0, k))
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            neighbours = graph[node]
            for (dst, time) in neighbours:
                if time + cost < distTo[dst]:
                    distTo[dst] = time + cost
                    # edgeTo[dst] = node
                    heapq.heappush(pq, (distTo[dst], dst))

        # the max one is the minimum time, we need to consider inf edge case
        return max(distTo) if max(distTo) != float("inf") else -1
```


# Reference

https://docs.google.com/presentation/d/1UHAU4IgEPYO3AJKYANd8XN8VDw5KZlt86HMLm9mJyyY/edit#slide=id.g99cc41691_0_200


