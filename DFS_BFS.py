#DFS
#주로 최단거리 구하는 문제에 적합

#시작노드를 방문처리후 stack에 push
#방문하지 않은 인접노드가 있다면 방문처리후 push
#방문하지 않은 인접노드가 없다면 stack에서 pop 후 2,3번반복

#재귀함수
def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

#반복문(낮은 node우선)
def dfs2(v):
    stack=[v]
    while stack:
        v=stack.pop()
        if visit[v]==0:
            visit[v]=1
            print(v,end=' ')
            temp=[]
            for i in graph[v]:
                if visit[i]==0:
                    temp.append(i)
            temp.sort(reverse=True)
            stack+=temp

#BFS
#경로의 트징을 저장해야하는 문제에 적합

#시작노드를 방문처리후 queue에 push
#큐에서 노드를 꺼내 해당노드의 인접노드중 방문하지 않은 노드를 모두 큐에 push
#반복

from collections import deque

def bfs(v):
    queue=deque()
    visit[v]=1
    queue.append(v)
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visit[i]==0:
                visit[i]=1
                queue.append(i)
