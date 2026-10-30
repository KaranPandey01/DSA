import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: adj[u] = [(v, weight), ...]
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[node][consecutive_count] stores the minimum cost to reach 'node'
        # with exactly 'consecutive_count' of labels[node] at the end of the path.
        # Max consecutive count possible is k.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Priority Queue stores tuples of (cost, current_node, consecutive_count)
        # Starting node 0 has 1 consecutive instance of its own character.
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            cost, u, consec = heapq.heappop(pq)
            
            # Target reached: due to Dijkstra properties, this is the optimal path
            if u == n - 1:
                return cost
                
            # If we found a shorter way to this state already, skip it
            if cost > dist[u][consec]:
                continue
                
            # Traverse neighboring nodes
            for v, weight in adj[u]:
                next_consec = consec + 1 if labels[u] == labels[v] else 1
                
                # Check if the transition breaks the consecutive constraint
                if next_consec <= k:
                    next_cost = cost + weight
                    if next_cost < dist[v][next_consec]:
                        dist[v][next_consec] = next_cost
                        heapq.heappush(pq, (next_cost, v, next_consec))
                        
        return -1
