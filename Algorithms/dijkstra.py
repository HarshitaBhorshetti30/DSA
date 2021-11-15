import heapq
from collections import defaultdict, deque

def findShortestPath(edges, src, vertices):
    adj_list = defaultdict(list)
    parent = dict()
    dist = defaultdict(lambda : float('inf'))
    for edge in edges:
        adj_list[edge[0]].append((edge[2],edge[1]))

    pq = []
    visited = set()
    heapq.heappush(pq, (0,src, ""))
    while pq:
        curr_cost, curr, p = heapq.heappop(pq)
        if curr in visited: continue
        dist[curr] = curr_cost
        parent[curr] = p
        visited.add(curr)
        for d,adj in adj_list[curr]:
            if adj in visited: continue
            if curr_cost + d < dist[adj]:
                heapq.heappush( pq, (curr_cost+d, adj, curr) )
    return dist, parent
   
edges = [
    (0,2,10),
    (0,1,5),
    (1,2,6),
    (2,3,3),
    (1,3,1)
]
vertices = [0,1,2,3]
print(findShortestPath(edges, 0, vertices))

