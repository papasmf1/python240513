# DemoRE.py 
#정규표현식 사용 
import re 

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#선택한 블럭을 주석: ctrl + / 
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print("---특정 단어---")
result = re.search("apple", "this is apple")
print(result.group())

print("---연도---")
result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

print("---우편번호---")
result = re.search("\d{5}", "우리 동네는 51222")
print(result.group())

