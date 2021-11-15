
class BellmanFord:
    def __init__(self, edges, n, src):
        self.edges = edges
        self.v = n
        self.src = src

    def findShortestPath(self,dest):
        dist = [float('inf')]*self.v
        dist[self.src] = 0
        parents = [-1]*self.v
        parents[self.src] = self.src

        for i in range(self.v-1):
            updated = False
            for edge in self.edges:
                u,v,cost = edge
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parents[v] = u
                    updated = True
                print(edge, dist)
            if updated == False: break

        path = [str(dest)]
        while dest != self.src:
            dest = parents[dest]
            path += [str(dest)]
        path.reverse()
        ans  = '->'.join(x for x in path)
        return dist,ans

edges = [
    (0,2,10),
    (0,1,5),
    (1,2,-6),
    (2,3,3),
    (1,3,-1)
]
bf = BellmanFord(edges, 4, 0)
print(bf.findShortestPath(3))

