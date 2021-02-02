#set
#mutable한 객체,순서가없음, unique한 값을 가진다
#내부원소는 mutable한 값을 가질 수 없다.(list,dic,set등을 원소로 가질 수 없)

#init
s={1,2,3}
s=set()

s.add(value)    #원소추가
s.update([3,4,5])   #여러데이터 한꺼번에 추가
s.remove(value)     #특정값 제거. 없으면 KeyError발생시킨다
s.discard(value)    #특정값 제거. 없어도 에러x

#set끼리의 여러 연산자들
c=a|b
c=a&b
c=a-b
c=a^b   #대칭차집합. 합집합-교집합

#연산 method들
c=a.union(b)
c=a.intersection(b)
c=a.difference(b)
c=a.symmetric_difference(b)

#기타 method
a.issubset(b)       #부분집합여부확인
a.issuperset(b)     #superset인지확인
a.isdisjoint(b)     #교집합이 없으면 T 있으면 F

