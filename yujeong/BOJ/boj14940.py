# 14940. 쉬운 최단거리 
import sys
input = sys.stdin.readline

from collections import deque

def dfs(n, m):
    q = deque()

    # 각 지점별 목적지까지 거리; -1로 초기화
    dist = [[-1] * m for _ in range(n)]

    # 원래 갈 수 없는 지점들은 거리 0으로 
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '2':        # 시작점
                q.append((i, j))        # queue에 추가
                dist[i][j] = 0
            elif arr[i][j] == '0':      # 갈 수 없는 곳
                dist[i][j] = 0    
    
    while q:
        px, py = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = px+dx, py+dy
            # 갈 수 없는 곳에 막히면 다른 방향으로 
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == '0':
                continue

            elif 0<=nx<n and 0<=ny<m and arr[nx][ny] == '1':
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[px][py] + 1     # 거리 업데이트되지 않은 곳이면 거리 추가하고
                    q.append((nx, ny))                  # queue에 추가 
    
    for v in dist:
        print(*v)

n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
dfs(n, m)
