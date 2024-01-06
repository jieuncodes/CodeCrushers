def solution(k):
    if(k==1):
        return 0
    def dfs(n, start, path, result):
        if n == 0:
            result.append(str("".join(path)))
            return
        for i in range(start, 10):
            dfs(n - 1, i + 1, path + [str(i)], result)

    result = []
    length = 1

    while len(result) < k:
        dfs(length, 0, [], result)
        print(result)

        length += 1
        if length > 10: 
            return -1
    return str(result[k - 1]) if k <= len(result) else "-1"

# "0"
# K=1

# "9"
# K=10

# "01"
# K=11

# "-1"
K=999999999

print(solution(K))




