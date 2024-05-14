# function1.py 
#1)함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

#2)호출 
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x 

#호출
retValue = swap(3,4)
print(retValue)

#지역변수와 전역변수 이름 충돌 
#전역변수 
x = 5 
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 10 
    return a+x 

#호출
print(func2(1))

print("---불변형식---")
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))

print("---가변형식---")
lst = [10,20,30]
print(id(lst))
lst.append(40)
print(id(lst))

#기본값명시
def times(a=10, b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자(매개변수명을 자세하기 기술)
def connectURI(server, port):
    url = "https://" + server + ":" + port 
    return url 

#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="multi.com"))

print(globals())

#오버로드를 지원안함(덮어쓰기)
def times(a):
    print(a)

def times(a=0,b=0):
    return a+b 

print(times())
print(times(a=5))
