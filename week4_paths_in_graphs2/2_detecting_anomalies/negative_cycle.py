import sys

def negative_cycle(adj, cost):
    # Initialize distance array with a very large number
    longest = []
    for item in cost:
        longest.extend(item)
    max_dist = sum(longest) + 1
    dist = [max_dist] * len(adj)
    prev = [-1] * len(adj)

    dist[0] = 0  # Start with the first vertex

    def relax(u, v, i):
        if dist[v] > dist[u] + cost[u][i]:
            dist[v] = dist[u] + cost[u][i]
            prev[v] = u
            return True
        return False

    # Bellman-Ford: Perform n-1 iterations of relaxation
    for i in range(len(adj)):
        for u in range(len(adj)):
            for j in range(len(adj[u])):
                v = adj[u][j]
                if relax(u, v, j) and i == len(adj) - 1:
                    # If we're on the nth iteration and a relaxation occurs, we have a negative cycle
                    return 1

    return 0

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
