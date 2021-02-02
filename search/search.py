#sequential search: O(N)

#binary search: O(logN)
#1. 데이터가 정렬되어 있어야 사용할 수 있다.

#recursive code
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

#iterative code
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

