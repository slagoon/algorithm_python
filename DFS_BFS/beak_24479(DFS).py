'''
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

'''



import sys
# 재귀 깊이 한도 해제
sys.setrecursionlimit(int(1e6))
# 빠른 입력받기
input = sys.stdin.readline

# input(): "5 5 1"
# input().split(): ["5", "5", "1"]
# map(int, input().split()): [5, 5, 1]
# n, m, r = 5, 5, 1
n, m, r = map(int, input().split())

# 1번 노드부터 n번 노드까지 "리스트(인접 노드)"를 갖도록 함
graph = [[] for i in range(n + 1)]

# 그래프 구축(인접 노드끼리 연결)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 노드부터 n번 노드까지 처음엔 방문하지 않은 것으로 처리
visited = [False] * (n + 1)

# 각 노드마다의 방문 순서
result = [0] * (n + 1)
cnt = 0


def dfs(x):
    global cnt
    # 현재 노드를 방문 처리
    visited[x] = True
    cnt += 1
    result[x] = cnt
    # 현재 노드와 인접한 노드를 하나씩 확인
    for y in graph[x]:
        # 인접 노드를 방문하지 않았다면, 재귀적으로 방문
        if not visited[y]:
            dfs(y)


for adj in graph:
    adj.sort()

dfs(r)  # r번 노드에서 출발

for i in range(1, n + 1):
    print(result[i])


# 출처 : https://www.acmicpc.net/problem/24479
