# DemoIndexing.py 
strA = """다중 라인으로
저장하는 
경우입니다.
"""

print(strA)

strB = "python is very powerful"
print(strB[0])
print(strB[0:6])
print(strB[:6])
print(strB[-3:])
print(strB[-8:])

#리스트 형식
colors = ["red", "blue", "green"]
print(colors)
print(len(colors))
print(type(colors))
#추가
colors.append("black")
colors.append("red")
colors.insert(1, "pink")
print(colors)

print(colors.index("blue"))
print(colors.count("red"))

#실수 
colors += ["black"]
colors += "red"
print(colors)

#삭제
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
#remove()
colors.remove("red")
#정렬
colors.sort()
print(colors)
#역정렬
colors.reverse()
print(colors)