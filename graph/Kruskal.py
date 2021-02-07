#간선데이터를 오름차순정렬
#간선이 싸이클을 발생시키지 않으면 mst에 포함시킨다
#O(ElogE)

v,e=map(int,input().split())
parent=[0]*(v+1)
edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)
