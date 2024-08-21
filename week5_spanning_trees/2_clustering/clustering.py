#Uses python3
import sys
import math

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def compute_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def clustering(x, y, k):
    n = len(x)
    edges = []

    # Step 1: Compute all pairwise distances and store them as edges
    for i in range(n):
        for j in range(i + 1, n):
            distance = compute_distance(x[i], y[i], x[j], y[j])
            edges.append((distance, i, j))
    
    edges.sort()

    # Step 2: Initialize Disjoint Set
    ds = DisjointSet(n)
    distances=[]
    # Step 3: Apply Kruskal's algorithm to form clusters
    for e in edges:
        dist, u, v = e
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            distances.append(dist)
    return distances[-k+1] if k>1 else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
