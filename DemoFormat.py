# DemoFormat.py 

#문자열 결합
for i in range(1,11):
    url = "https://www.multi.com/?page=" + str(i) 
    print(url)

print("---정렬방식 지정---")
for x in range(1,10):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬방식 지정---")
for x in range(1,10):
    print(x, "*", x, "=", str(x*x).rjust(5))

print("---정렬방식 지정---")
for x in range(1,10):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:c}".format(65))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))

