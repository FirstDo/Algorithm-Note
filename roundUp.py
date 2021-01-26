#python의 반올림은 사사오입(0.5일 경우 짝수일땐 버리고 홀수일땐 올림)
#따라서 직접 구현해야함

def roundUp(n):
    return int(n)+1 if(n-int(n))>=0.5 else int(n)

