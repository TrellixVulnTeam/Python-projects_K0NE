# Uses python3

import sys


def negative_cycle(adj, cost):
    return negative_cycle_util(adj, cost)


def negative_cycle_util(adj, cost):
    n = len(adj)
    dist = [sys.maxsize] * n
    dist[0] = 0
    for i in range(n):
        for j in range(n):
            for k in range(len(adj[j])):
                # if dist[j] < sys.maxsize:
                if dist[adj[j][k]] > dist[j] + cost[j][k]:
                    dist[adj[j][k]] = dist[j] + cost[j][k]
                    if i == n - 1:
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
