import sys
import heapq

def distance(adj, cost, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    priority_queue = [(0, s)]  # (distance, node)
    visited = set()  # To track visited nodes

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if u in visited:
            continue
        visited.add(u)

        # Early exit if we've reached the target node
        if u == t:
            return current_dist

        for j in range(len(adj[u])):
            v = adj[u][j]
            weight = cost[u][j]

            # Relaxation step
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(priority_queue, (dist[v], v))  # Push with updated distance

    return dist[t] if dist[t] != float('inf') else -1

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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
