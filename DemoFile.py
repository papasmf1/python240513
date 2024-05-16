# DemoFile.py 

#쓰기:유니코드로 작업  
#raw string notation: r을 앞에 지정 
f = open(r"c:\work\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째라인\n")
f.close() 

#기존 파일에 첨부하는 경우:append, read, write
f = open(r"c:\work\test.txt", "a+", encoding="utf-8")
f.write("네번째라인추가\n")
f.close() 


#읽기 
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
result = f.read() 
print(result)

#파일 포인터를 처음으로 돌리기 
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

#다시 처음
f.seek(0)
lst = f.readlines() 
for item in lst:
    print(item, end="")


f.close() 
