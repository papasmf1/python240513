# DemoTupleSet.py 

#튜플
tp = (1,2,3)
print(len(tp))
print(type(tp))
print(tp.count(1))

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출
result = calc(3,4)
print(result[0])
print(result[1])

print( "id: %s, name: %s" % ("kim", "김유신") )

args = (5,6)
# *는 튜플이라는 힌트 
print(calc(*args))

#Set형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a | b)
print(a & b)
print(a - b)

#형식변환
b = list((10,20,30))
print(b)
b.append(40)
print(b)

