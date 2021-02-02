#initalize list
#one dimensional list
onelist=[0]*length
#two dimesional list
twolist=[[0]*col for _ in range(row)]

#list function
list=[]
list.append()		#:리스트에 원소를 하나 삽입
list.sort()		#:기본 정렬 기능으로 오름차순으로 정렬	O(NlogN)
list.sort(reverse=True)	#:기본정렬기능으로 내림차순으로 정렬	O(NlogN)
#key로 정렬기준 설정가능. ex) key=lambda x:(x[0],x[1])

list.reverse()		#:리스트의 원소의 순서를 모두 뒤집는다	O(N)
list.insert(index,value)#:특정 index위치에 value값을 삽입	O(N)
list.count(value)	#:list에서 value값을 가진 데이터의 개수	O(N)
list.remove(value)	#:list에서 value값을 가진 데이터를 제거. 하나만제거한다. O(N)
list.index(value)	#:list에서 value값이 있으면 그 index를 return. 없으면 ValueError발생.O(N)
list.pop()		#:list의 맨 마지막 요소를 return한후 그 요소를 삭제	O(1)
list.pop(i)		#:list에서 i번째 요소를 return하고 그 요소를 삭제	O(N)
list.extend(list2)	#:list에 list2를 더해줌	//list+=list2로도 쓸 수 있다

#list 컴프리헨션 사용예
array=[i for i in range(20) if i%2==1]          #0~20미만 홀수로 리스트 구성
array=[(i,j) for i in range(n) for j in range(m) if graph[i][j]==value] #리스트에서 특정값을 찾아 그 index로 리스트 구

