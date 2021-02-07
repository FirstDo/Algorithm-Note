#다익스트라 알고리즘

#쉬운버전 O(V^2)
import sys
input=sys.stdin.readline
INF=int(1e9)

#입력받고,  visited배열과 distance배열, graph를 만든다.
n,m=map(int,input().split())
start=int(input())
qraph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    #최단거리가 가장 짧은 노드를 찾는다.
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    #start부터 각 노드까지의 거리 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        #원래 distance>현재노드를 통해가는 거리 이면 바꿔준다.
        for j in graph[now]:
            cost=distance[now]+j[1]

            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

#어려운버전!!중요!!!! O(ElogV)
import heapq
import sys
input=sys.stdin.readline
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    #시작점을 push하고 거리설정
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        #이미처리된적이 있으면 무시
        if distance[now]<dist:
            continue
        #인접한 노드들 확인
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0])

dijkstra(start)























