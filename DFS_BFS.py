#DFS
#시작노드를 방문처리후 stack에 push
#방문하지 않은 인접노드가 있다면 방문처리후 push
#방문하지 않은 인접노드가 없다면 stack에서 pop 후 2,3번반복

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end==' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#BFS
#시작노드를 방문처리후 queue에 push
#큐에서 노드를 꺼내 해당노드의 인접노드중 방문하지 않은 노드를 모두 큐에 push
#반복

from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    whuke queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
