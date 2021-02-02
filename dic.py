#construct
d=dic()
d={}

#add
d[key]=value    #key는 immutable한 값을써야한다

#delete
del d[key]      #key,value쌍을 지운
d.clear()       #모두지운다

#get
d[key]          #key를 이용해 value를 얻을 수 있다.
d.get(key)      #위와 같은 기능이지만 오류를 발생시키지 않음.

#function
d.keys()        #key만을 모아서 dict_keys 객체를 돌려줌.
d.values()      #value만을 모아서 dict_values 객체를 돌려줌



