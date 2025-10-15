def minimum_total_with_path(triangle):
    n = len(triangle)
    
    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
    
    min_sum = min(dp[-1])
    min_index = dp[-1].index(min_sum)

    path = []
    i, j = n - 1, min_index
    path.append(triangle[i][j])
    
    for i in range(n - 2, -1, -1):
        if j == 0:
            j = 0
        elif j == len(triangle[i + 1]) - 1:
            j = j - 1
        else:
            if dp[i][j-1] + triangle[i+1][j] == dp[i+1][j]:
                j = j - 1
            else:
                j = j
        path.append(triangle[i][j])
    
    path.reverse()
    return min_sum, path


if __name__ == "__main__":
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sum1, path1 = minimum_total_with_path(triangle1)
    print(f"Треугольник 1: {triangle1}")
    print(f"Минимальный путь: {' → '.join(map(str, path1))}")
    print(f"Результат: {sum1}")

    triangle2 = [[-1],[2,3],[1,-1,-3],[4,2,1,3]]
    sum2, path2 = minimum_total_with_path(triangle2)
    print(f"Треугольник 2: {triangle2}")
    print(f"Минимальный путь: {' → '.join(map(str, path2))}")
    print(f"Результат: {sum2}")
