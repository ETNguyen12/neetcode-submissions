class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append((time, target))
        
        min_times = {}
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in min_times:
                continue
            min_times[node] = time
            for extra, target in adj[node]:
                if target not in min_times:
                    heapq.heappush(heap, (time + extra, target))

        return max(min_times.values()) if len(min_times) == n else -1