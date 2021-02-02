#에라토스테네스의 체
def getPrimaryNum(N):
    nums=[True]*(N+1)
    for i in range(2,len(nums)//2+1):
        if num[i]==True:
            for j in range(i,N,i):
                num[j]=False
    return [i for i in range(2,N) if nums[i]==True]
