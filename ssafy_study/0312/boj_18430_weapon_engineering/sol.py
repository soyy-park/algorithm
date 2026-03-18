import sys
sys.stdin = open('input.txt')

<<<<<<< Updated upstream
def boomerang_type(r, c, n, gangdo):
    if n == 0:
        if r+1 < N and c-1 >= 0:
            if not visited[r][c] and not visited[r][c-1] and not visited[r+1][c]:
                visited[r][c], visited[r][c-1], visited[r+1][c] = 1, 1, 1
                tmp = arr[r][c] * 2 + arr[r][c-1] + arr[r+1][c]
                make_boomerang(r, c+1, gangdo + tmp)
                visited[r][c], visited[r][c-1], visited[r+1][c] = 0, 0, 0

    elif n == 1:
        if r-1 >= 0 and c-1 >= 0:
            if not visited[r][c] and not visited[r-1][c] and not visited[r][c-1]:
                visited[r][c], visited[r-1][c], visited[r][c-1] = 1, 1, 1
                tmp = arr[r][c] * 2 + arr[r-1][c] + arr[r][c-1]
                make_boomerang(r, c+1, gangdo + tmp)
                visited[r][c], visited[r-1][c], visited[r][c-1] = 0, 0, 0

    elif n == 2:
        if r-1 >= 0 and c+1 < M:
            if not visited[r][c] and not visited[r-1][c] and not visited[r][c+1]:
                visited[r][c], visited[r-1][c], visited[r][c+1] = 1, 1, 1
                tmp = arr[r][c] * 2 + arr[r-1][c] + arr[r][c+1]
                make_boomerang(r, c+1, gangdo + tmp)
                visited[r][c], visited[r-1][c], visited[r][c+1] = 0, 0, 0

    elif n == 3:
        if r+1 < N and c+1 < M:
            if not visited[r][c] and not visited[r][c+1] and not visited[r+1][c]:
                visited[r][c], visited[r][c+1], visited[r+1][c] = 1, 1, 1
                tmp = arr[r][c] * 2 + arr[r][c+1] + arr[r+1][c]
                make_boomerang(r, c+1, gangdo + tmp)
                visited[r][c], visited[r][c+1], visited[r+1][c] = 0, 0, 0

def make_boomerang(r, c, gangdo):
    global max_gangdo

    if c == M:
        r, c = r+1, 0
        if r == N:
            max_gangdo = max(gangdo, max_gangdo)
            return
    
    make_boomerang(r, c+1, gangdo)

    for k in range(4):
        boomerang_type(r, c, k, gangdo)
=======
def make_boomerang(r, c):
    if c == M:
        r, c = r+1, 0
        if r == N:
            return
    if visited[r][c]:
        for i in range(N):
            print(visited[i])
        print (r, c)
        return
    
    # ㄱ
    if r+1 < N and c+1 < N:
        if not visited[r+1][c+1] and not visited[r][c+1]:
            print(r, c)
            visited[r][c], visited[r+1][c], visited[r][c+1] = 1, 1, 1
            make_boomerang(r, c+1)
            visited[r][c], visited[r+1][c], visited[r][c+1] = 0, 0, 0
    
    if r+1 < N and c-1 >= 0:
        if not visited[r][c-1] and not visited[r+1][c]:
            visited[r][c], visited[r][c-1], visited[r+1][c] = 1, 1, 1
            make_boomerang(r, c+1)
            visited[r][c], visited[r][c-1], visited[r+1][c] = 0, 0, 0
>>>>>>> Stashed changes

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
<<<<<<< Updated upstream

gangdo = 0
max_gangdo = 0
make_boomerang(0, 0, 0)
print(max_gangdo)
=======
print(visited)
make_boomerang(0, 0)
>>>>>>> Stashed changes
