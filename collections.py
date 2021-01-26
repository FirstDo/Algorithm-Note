collections.Counter(a): a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환

import collections

a=[1,1,2,2,2,3,3]
print(collections.Counter(a))

# =>Counter({2:3,1:2,3:2})

#most_common()함수- 최빈값 구하기

a=[1,1,1,2,3,2,3,245,9]

print(collections.Counter(a).most_common(3))
=> [(1,3),(2,2),(3,2)]
