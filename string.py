#문자열

string.count('c')	#:c의 개수를 반환
string.find('c')	#:c가 처음으로 나온 위치를 반환 없으면 -1
string.index('c')	#:find와 동일하지만 없으면 error발생
"c".join(string)	#:string의 각각의 문자사이에 c삽입
string.upper() / string.lower()	#:대소문자변경
string.rstrip() / string.lstrip() /string.strip()	#:공백지우기
string.replace(s1,s2)	#:s1을 s2로 바꾼다
string.split()	#:문자열 나누기
