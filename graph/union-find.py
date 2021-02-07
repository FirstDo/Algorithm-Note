#무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.
#두 노드간에 union연산을 수행할때, 루트노드가 같다면 cycle이 발생한 것이다.

def find_parent(parent,x):
    if parent[x]!=x:
        #경로압축
        parent[x]=find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parnet(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

