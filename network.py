class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            if self.rank[ri] > self.rank[rj]:
                self.parent[rj] = ri
            else:
                self.parent[ri] = rj
                if self.rank[ri] == self.rank[rj]:
                    self.rank[rj] += 1

def network(edges, computers):
    n = max(max(u, v) for u, v, _ in edges) + 1
    dsu = DisjointSet(n)
    computers_set = set(computers)
    edges.sort(key=lambda x: x[2])
    mst = []

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            if u in computers_set and v in computers_set:
                dsu.union(u, v)
                mst.append((u, v, w))
            elif u in computers_set or v in computers_set:
                ru, rv = dsu.find(u), dsu.find(v)
                if any(comp in computers_set for comp in [ru, rv]):
                    dsu.union(u, v)
                    mst.append((u, v, w))
    
    mst_edges = set()
    for u, v, w in mst:
        mst_edges.add((u, v))
        mst_edges.add((v, u))

    connected_computers = set()
    for u, v in mst_edges:
        if u in computers_set:
            connected_computers.add(u)
        if v in computers_set:
            connected_computers.add(v)
            
    if connected_computers != computers_set:
        return []

    return mst