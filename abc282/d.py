from collections import deque

n, m = list(map(int, input().split(" ")))

edges = [[] for _ in range(n + 1)]
color = [0 for _ in range(n + 1)]

for i in range(m):
    u, v = list(map(int, input().split(" ")))
    edges[u].append(v)
    edges[v].append(u)


def solve(n):
    waiting = deque()
    tmp_color = 1
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = tmp_color
            for nex_node in edges[i]:
                color[nex_node] = -tmp_color
                waiting.append(nex_node)
            while len(waiting):
                cur_node = waiting.pop()
                for nex_node in edges[cur_node]:
                    if color[nex_node] == color[cur_node]:
                        return 0
                    elif color[nex_node] == 0:
                        color[nex_node] = -color[cur_node]
                        waiting.append(nex_node)
        tmp_color += 1
    return tmp_color


res = solve(n)
if res == 0:
    print(0)
else:
    ans = n * (n - 1) // 2 - m
    for i in range(1, res):
        tmp = color.count(i)
        ans -= tmp * (tmp - 1) // 2
        tmp = color.count(-i)
        ans -= tmp * (tmp - 1) // 2
    print(ans)
