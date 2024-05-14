# DemoDict.py 
fruits = {"apple":"red", "banana":"yellow"}
print(fruits)
print(len(fruits))

#검색
print(fruits["apple"])

#입력
fruits["kiwi"] = "green"
print(fruits)

#삭제
del fruits["apple"]

for item in fruits.items():
    print(item)

for k,v in fruits.items():
    print(k, v)

print("---장비관리---")
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(len(device))
#입력
device["맥북"] = 15 
#수정
device["아이폰"] = 6 
print(device)
#삭제
del device["아이폰"]
print(device)
#검색
print(device["맥북"])

print("---명함관리---")
phone = {"kim":"111", "lee":"222", "park":"333"}
print(phone.keys())
print(phone.values())
print("kim" in phone)
print("moon" not in phone)

#파이썬은 항상 참조를 전달(Pass By Reference)
p = phone 
p["kang"] = "123"
print(p)
print(phone)
print(id(p), id(phone))


print("---bool, 논리식---")
isRight = True
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print( bool(0) )
print( bool(1) )
print( bool("") )
print( bool("demo") )
print( bool([]) )
print( bool([1,2,3]) )




