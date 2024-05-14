# DemoLoop.py 
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---for in루프---")
for i in range(5):
    print(i)

lst = ["apple", 100, 3.14]
for item  in lst:
    print(item)

colors = {"apple":100, "orange":200}
for k,v in colors.items():
    print(k,v)

print("---구구단---")
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

print("---break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 1:
        continue 
    print("Item:{0}".format(i))

print("---range()함수---")
lst = list(range(1,11))
print(lst)
print(list(range(2000,2025)))
print(list(range(1,32)))

print("---리스트 컴프리헨션---")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )
tp = ("apple", "orange")
print( [len(i) for i in tp] )
d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()] )

print("---필터링---")
lst = [10, 25, 30]

itemL = filter(None, lst)
for item in itemL:
    print(item)

print("---필터링 함수 있는 경우---")
def getBiggerThan20(i):
    return i>20

lst = [10, 25, 30 ]

itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)


