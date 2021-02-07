#진입차수가 0인 노드를 큐에 넣는다
#큐에서 원소를 꺼내, 해당 노드에서 출발하는 간선을 제거, 진입차수가 0이된 노드를 큐에 넣는다. 반복
#O(V+E)

#v,e

indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]

for _ in range(e):
    a,b,=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft():
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
