#Uses python3
import sys
import math
class DisjointSet:
    def __init__(self, n):
        # Initialize the parent and rank arrays
        self.parent = []
        self.rank = []

        # Create a disjoint set with `n` elements
        for i in range(n):
            self.make_set(i)

    def make_set(self, x):
        """Initialize the set with a single element."""
        self.parent.append(x)  # Each element is its own parent initially
        self.rank.append(0)     # Rank is initialized to 0

    def find(self, x):
        """Find the representative of the set containing `x` with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing `x` and `y` with union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
def compute_distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
def minimum_distance(x, y):
    result = 0.
    n= len(x)
    edges=[]
    d = DisjointSet(n)
    for i in range(n-1):
        for j in range(i+1,n):
           edges.append((compute_distance((x[i],y[i]),(x[j],y[j])),i,j))
    edges.sort()
    for i in range(n):
        d.make_set(i)
    for e in edges:
        if d.find(e[1])!=d.find(e[2]):
            result+=e[0]
            d.union(e[1],e[2])
        
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
