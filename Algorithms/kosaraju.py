from collections import defaultdict


class Kosaraju:

    def __init__(self, adj_list):
        self.visited = set()
        self.stack = []
        self.adj_list = adj_list
        self.compressed_adj = defaultdict(set)

    def DFS1(self, v):
        for n in self.adj_list[v]:
            if n not in self.visited:
                self.visited.add(n)
                self.DFS1(n)
        self.stack.append(v)
        return

    def reverseGraph(self):
        reversed_adj_list = defaultdict(list)
        for k,v in self.adj_list.items():
            for neighbor in v:
                reversed_adj_list[neighbor].append(k)
        self.adj_list = reversed_adj_list

    def DFS2(self, v):
        for n in self.adj_list[v]:
            if n not in self.visited:
                self.visited.add(n)
                return [v] + self.DFS2(n)
        return [v]

    def findSCC(self):
        ans = []
    
        # Perform DFS 
        for v in self.adj_list:
            if v not in self.visited:
                self.visited.add(v)
                self.DFS1(v)

        # Reversing Graph
        self.reverseGraph()
        self.visited = set()

        # Perform DFS for each vertex in stack for SCC
        for i in range(len(self.stack)):
            curr = self.stack.pop()
            if curr not in self.visited:
                self.visited.add(curr)
                scc = self.DFS2(curr)
                ans.append(scc)
        return ans

    def findMinimumUsers(self, ans):
        users = []
        incoming, who = dict(), dict()

        # create a who map for representative and actual node
        for scc in ans:
            incoming[scc[0]] = 0
            for v in scc:
                who[v] = scc[0]

        # create a compressed graph
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                if who[v] != who[neighbor] and who[neighbor] not in self.compressed_adj[who[v]]:
                    self.compressed_adj[who[v]].add(who[neighbor])
                    incoming[who[neighbor]] += 1

        # find users with incoming edge 0
        for v in incoming:
            if incoming[v] == 0:
                users.append(v)

        return users


adj_list = {
    0 : [1,6],
    1 : [2],
    2 : [0,3],
    3 : [2,4],
    4 : [5],
    5 : [3],
    6 : []
}

k = Kosaraju(adj_list)
scc = k.findSCC()
print(scc)
print(k.findMinimumUsers(scc))

