import sys

def negative_cycle(adj, cost):
    n = len(adj)
    dist = [float('inf')] * n
    dist[0] = 0  # Start with the first vertex (assuming 0-indexed)
    
    # Bellman-Ford algorithm: Perform n-1 relaxations
    for i in range(n - 1):
        for u in range(n):
            for j in range(len(adj[u])):
                v = adj[u][j]
                weight = cost[u][j]
                if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for u in range(n):
        for j in range(len(adj[u])):
            v = adj[u][j]
            weight = cost[u][j]
            if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                return 1  # Negative cycle detected

    return 0  # No negative cycle

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
