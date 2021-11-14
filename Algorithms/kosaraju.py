from collections import defaultdict


class Kosaraju:

    def __init__(self, adj_list):
        self.visited = set()
        self.stack = []
        self.adj_list = adj_list

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

        print(self.stack)

        # Reversing Graph
        self.reverseGraph()
        self.visited = set()

        print(self.adj_list)

        # Perform DFS for each vertex in stack for SCC
        for i in range(len(self.stack)):
            curr = self.stack.pop()
            print(curr)
            if curr not in self.visited:
                self.visited.add(curr)
                scc = self.DFS2(curr)
                print(scc)
                ans.append(scc)

        return ans


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
print(k.findSCC())
