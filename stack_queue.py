#stack의 경우 list를 그대로 사용
stack=[]
stack.append(1)
stack.pop()

#queue의 경우 collections의 deque를 사용
from collections import deque

queue=deque()

queue.append(5)
queue.popleft()

#list() method를 이용하면 리스트로 변환가능
#queue.reverse()도 가능

