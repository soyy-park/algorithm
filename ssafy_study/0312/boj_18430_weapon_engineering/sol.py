import sys
sys.stdin = open('input.txt')

def make_boomerang(r, c):
    # ㄱ
    if r+1 < N and c-1 >= 0:
        if not visited[r][c-1] and not visited[r+1][c]:
            visited[r][c-1] = 1
            visited[r+1][c] = 1
            make_boomerang(r+1, c-1)
            visited[r][c]

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(visited)