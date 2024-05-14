# function2.py

#가변인자
def union(*ar):
    #지역변수
    result = [] 
    for item in ar:
        for x  in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda a:a*a)(3) )
print(globals())

print("---필터링 함수 있는 경우---")
def getBiggerThan20(i):
    return i>20

lst = [10, 25, 30 ]

itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("---람다함수---")
itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)

