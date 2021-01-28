#2차원 배열 관련..
#2차원 배열에서 특정값 찾기

ans=[(i,j) for i in range(n) for j in range(m) if graph[i][j]==value]
print(ans)

#2차원 배열의 정렬기준
#x,y 오름차순으로 정렬
sorted(arr,key=lambda x:(x[0],x[1]))

