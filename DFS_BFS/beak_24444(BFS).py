'''
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.
'''


import sys
# 빠른 입력받기
input = sys.stdin.readline

from collections import deque

# input().split(): ["5", "5", "1"]
# map(int, input().split()): 5, 5, 1

n, m, r = map(int, input().split())

# 정점의 수가 N개이므로, N + 1개만큼 할당
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    # u와 인접한 노드는 v
    graph[u].append(v)
    # v와 인접한 노드는 u
    graph[v].append(u)

# 인접 노드는 오름차순으로 방문
for adj in graph:
    adj.sort()

# BFS를 위해서는 큐가 필요
queue = deque()

# 시작 노드는 r
queue.append(r)
visited[r] = True

# 방문 결과를 담기 위한 배열
result = [0] * (n + 1)
cnt = 0

while queue:
    # 큐에서 노드를 꺼내기
    x = queue.popleft()
    cnt += 1
    result[x] = cnt
    # 꺼낸 노드와 인접한 노드를 하나씩 확인
    for y in graph[x]:
        # 방문하지 않은 인접 노드라면
        if not visited[y]:
            # 인접 노드를 방문 처리
            visited[y] = True
            # 큐에 인접 노드를 추가
            queue.append(y)

# 방문 결과 출력
for i in range(1, n + 1):
    print(result[i])


# 출처 : https://www.acmicpc.net/submit/24444/80841382
