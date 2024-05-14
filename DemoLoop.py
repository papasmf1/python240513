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
