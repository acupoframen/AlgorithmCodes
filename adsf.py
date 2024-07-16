def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    rootX = find(x, parent)
    rootY = find(y, parent)
    if rootX != rootY:
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]

def min_red_edges(n, data):
    parent = list(range(n))
    size = [1] * n
    answer = 0

    for color in data:
        roots = list(set(find(i, parent) for i in range(n)))
        if len(roots) == 1:
            break

        roots.sort(key=lambda x: size[x])

        if color == 0:
            u, v = roots[0], roots[1]
            answer += size[u] * size[v]
        else:
            u, v = roots[0], roots[1]

        union(u, v, parent, size)

    return answer

# Test input
n = 5
data = [0, 0, 0, 1]
output = min_red_edges(n, data)
print(output)
