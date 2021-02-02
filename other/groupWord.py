#**그룹단어의 개수를 찾는문제
#aabba (x)
#aaabb (o)

import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for _ in range(n):
    word=input().rstrip()
    error=False
    for i in range(len(word)-1):
    	#연속된 단어의 끝을 찾아서, 그 이후의 문자열에 해당 단어가 있는지 검사
        if word[i]!=word[i+1]:
            new_word=word[i+1:]
            if new_word.find(word[i])!=-1:
                error=True
                break
    if error==False:
        cnt+=1
print(cnt)

