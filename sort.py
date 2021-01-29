#python의 기본 정렬 라이브러리는 c언어 기반이여서 매우 빠르다.

#1. selction sort
array=[7,5,9,0,3,1,6,2,4,8]
min_index=array[0]
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print(array)

#2. insertion sort: 데이터가 정렬이 잘되있을수록 빠르게 동작함
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)

#3. Quick sort: 평균 nlogn 그러나 데이터가 이미 정렬되어 있는 경우 n^2
import sys
input=sys.stdin.readline

array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    #원소가 1개인 경우 종료
    if start>=end:
        return
    #피벗과 left,right범위 설정
    pivot=start
    left=start+1
    right=end
    #교차되기 전까진 반복
    while left<=right:
        #pivot보다 큰 데이터 찾을때까지 left++
        while left<=end and array[left]<=array[pivot]:
            left+=1
        #pivot보다 작은 데이터 찾을때까지 right++
        while right>start and array[right]>=array[pivot]:
            right-=1
        #교차되었으면 right와 pivot swap
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        #교차전이면 left와 right swap
        else:
            array[left],array[right]=array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)


quick_sort(array,0,len(array)-1)
print(array)

#4. 계수 정렬: 모든 범위를 담을수있는 리스트 선언해야함.
#데이터의 개수가 N, 데이터 중 최대값이 K라면 O(N+K)를 보장


array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1


for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
