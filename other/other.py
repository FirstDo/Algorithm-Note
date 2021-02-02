#재귀함수 한계설정
import sys
sys.setrecursionlimit(1000000)

#시간복잡도
#보통 1초에 2,000만번 정도 수행한다고 생각. ex) N=100만이면 NlogN이 필요하다.

reversed(range(n)):	                        #거꾸로 반복할 수 있음
lfunc=lambda arguments: expression	        #함수호출, 바로사용 둘다 가능
list(filter(lfunc(arr))), list(map(lfunc(arr))) #filter와 map과 같이 사용함
#eval함수는 025같은 거 처리 불가능

#extended slices
arr[a:b:c]      #a부터 b까지 c의 간격으로 배열을 만들어라
