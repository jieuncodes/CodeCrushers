def solution(n, edges, blackouts):
    parent = [i for i in range(n+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for u, v in edges:
        if u not in blackouts and v not in blackouts:
            union(u, v)
    
    direct_connections = sum(1 for u, v in edges if (u == 1 and v in blackouts) or (v == 1 and u in blackouts))

    indirect_connections = sum(1 for u in blackouts if find(u) == 1)

    min_faults = direct_connections
    max_faults = direct_connections + indirect_connections

    return [min_faults, max_faults]



# res = [3,5]
n = 7
edges = [[1,2],[1,3],[1,4],[2,4],[3,5],[4,6],[4,5],[4,7]]
blackouts = [4, 6, 7]

# res = [4,7]
# n = 9
# edges = [[2,3],[3,4],[4,6],[6,9],[5,7],[2,5],[1,3],[1,5],[1,6],[1,8],[1,7],[1,9]]
# blackouts = [4,6,8]


print(solution(n, edges, blackouts))



