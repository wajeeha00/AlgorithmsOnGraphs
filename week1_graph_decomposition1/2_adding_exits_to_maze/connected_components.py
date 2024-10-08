#Uses python3

import sys
def explore(v,adj,visited):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(w,adj,visited)
    return visited


def number_of_components(adj):
    result = 0
    visited = [False] * len(adj)
    while visited.count(True)!=len(adj):
        for i in range(len(adj)):
            if not visited[i]:
                visited=explore(i,adj,visited)
                result+=1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
