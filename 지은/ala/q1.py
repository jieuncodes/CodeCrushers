def solution(n, edges, blackouts):
    a,b,c = 0,0,0

    for edge in edges:
        if edge[0] in blackouts and edge[1] in blackouts:
            c += 1
        elif edge[0] in blackouts or edge[1] in blackouts:
            b += 1
        else:
            a += 1
    
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
    
    cnt=0
    print(parent)
    for edge in edges:
        if len(set(parent)) == 1:
            break
        if edge[0] == 1 and parent[edge[1]] == 1 and edge[1] not in blackouts:
            cnt +=1
        elif edge[1] == 1 and parent[edge[0]] == 1 and edge[0] not in blackouts:
            cnt +=1

    

    return [b, b+c+cnt-1]






# res = [3,5]
n = 7
edges = [[1,2],[1,3],[1,4],[2,4],[3,5],[4,6],[4,5],[4,7]]
blackouts = [4, 6, 7]

# res = [4,7]
# n = 9
# edges = [[2,3],[3,4],[4,6],[6,9],[5,7],[2,5],[1,3],[1,5],[1,6],[1,8],[1,7],[1,9]]
# blackouts = [4,6,8]


print(solution(n, edges, blackouts))



