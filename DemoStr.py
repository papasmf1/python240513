# DemoStr.py 
#순회가능한 열거형식 
strA = "python is very powerful"
lst = [100, 200, 300]
tp = (10, 20, 30)

print(strA[:6])
print(lst[1])
print(tp[2])

names = ["전우치","이순신","박문수"]
for name in names:
    print("안녕하세요 {0}님! 여름입니다.".format(name))
    print("=" * 40)

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))
print("demo.ppt".startswith("demo"))
print("demo.ppt".endswith("ppt"))
print(strA.upper())
print("---숫자와 알파벳으로 구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---공백문자 제거---")
data = "<<<  spam and ham  >>>"
result = data.strip("<> ") 
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
print("---리스트로 변환---")
lst = result2.split() 
print(lst)
print(":)".join(lst))



