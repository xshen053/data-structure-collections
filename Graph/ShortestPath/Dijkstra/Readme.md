# Classic Dijkstra

## dijkstra 几个注意事项

1. pq 维护的 distance 是 node 的全局 distance，而不是根据单条 edge 排序的 （即 pq 里的 dis 是到某个 node 的 smallest dist，而不是根据 edge 来选取的）
2. visited 确保不会进行多余的计算
3. 对于每一个当前 node，我们都会找到它到它 neighbour 的 shortest path。并不是根据 prev_node 来更新，每个 pq 里面的 distance 都是全局 smallest 的

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
