N = int(input())
visited = [False] * N
QueenLocation = [0] * N
cnt = 0


def DFS(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        if not visited[i]:  
            QueenLocation[depth] = i  

            isQLocated = False
            for j in range(depth):
                   #상하좌우 탐색
                if abs(QueenLocation[depth] - QueenLocation[j]) == abs(depth-j):                   
                    isQLocated = True
                    break

            if not isQLocated:
                visited[i] = True
                DFS(depth+1)
                visited[i] = False


DFS(0)
print(cnt)