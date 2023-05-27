from collections import deque


def solve(n, colors, edges):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[0][n - 1] = 0
    waiting = deque()
    for next_node1 in edges[0]:
        for next_node2 in edges[n - 1]:
            if (
                colors[next_node1] != colors[next_node2]
                and visited[next_node1][next_node2] == -1
            ):
                waiting.append([next_node1, next_node2])
                visited[next_node1][next_node2] = 1
    while len(waiting):
        tmp1, tmp2 = waiting.popleft()
        if tmp1 == n - 1 and tmp2 == 0:
            return visited[n - 1][0]
        for next_node1 in edges[tmp1]:
            for next_node2 in edges[tmp2]:
                if (
                    colors[next_node1] != colors[next_node2]
                    and visited[next_node1][next_node2] == -1
                ):
                    waiting.append([next_node1, next_node2])
                    visited[next_node1][next_node2] = visited[tmp1][tmp2] + 1
    return -1


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))
    edges = [[] for _ in range(n)]
    for i in range(m):
        u, v = list(map(int, input().split(" ")))
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)
    print(solve(n, c, edges))
