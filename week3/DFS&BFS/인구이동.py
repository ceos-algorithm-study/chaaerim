from collections import deque
from operator import truediv

n, l, r=map(int, input().split())

# 인구수 입력 
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

visited=[]
# 노드 하나씩 꺼내오기 
for i in len(graph):
    for j in len(graph[i]):
        queue=deque(graph[i][j])
        # visited[graph[i][j]]=True
        while queue:
            v=queue.popleft()
            
