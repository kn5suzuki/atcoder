n, m = list(map(int, input().split(" ")))
edges = [[] for _ in range(n)]
for _ in range(n):
    u,v = list(map(int, input().split(" ")))
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

k = int(input())
queries = []
for _ in range(k):
    p,d = list(map(int, input().split(" ")))
    queries.append((p-1,d))

def solve(curr_node, colors, visited, i):
    if i == k:
        return colors
    visited[curr_node] = True
    if colors[curr_node] == 2:
        return -1
    colors[curr_node] = 1

    queue = [curr_node]
    while queue:
        current = queue.pop()
        for next in edges[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    if distance < k[i][1]:
        colors[curr_node] = 1
        for next in edges[curr_node]:
            if colors[next] == 0:
                colors = solve(next, colors, distance+1, i)
    elif distance == k[i][1]:
        colors[curr_node] = 2
        colors = 
    queue = [0]
    while queue:
        current = queue.pop()
        for next in edges[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    for query in queries:
        if visited[query[0]]:
            print("Town")
        else:
            print("Road")