# わからん
def dfs(current_node, ans):
    if ans >= limit:
        return limit
    visited[current_node] = True
    ans += 1
    for next_node in edges[current_node]:
        if not visited[next_node]:
            ans = dfs(next_node, ans)
    visited[current_node] = False
    return min(ans, limit)


n, m = list(map(int, input().split(" ")))
edges = [[] for _ in range(n)]
for i in range(m):
    u, v = list(map(int, input().split(" ")))
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)

visited = [False for _ in range(n)]
limit = 10**6
ans = dfs(0, 0)
print(ans)
