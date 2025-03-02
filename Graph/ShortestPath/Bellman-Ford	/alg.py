class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        for v in range(1, n + 1):
            for edge in times:
                if dist[edge[0]] + edge[2] < dist[edge[1]]:
                    dist[edge[1]] = dist[edge[0]] + edge[2]
        
        minimum_time = max(dist[1:])
        return minimum_time if minimum_time != float('inf') else -1
