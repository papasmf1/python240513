# Chap05_self누락_이름충돌.py
#전역변수 
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수 
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그 
        print(self.strName)

g = DemoString()
g.set("First Message")
g.print()
