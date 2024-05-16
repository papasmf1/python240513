#Chap05_부모 클래스_자식 클래스.py
#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
        self.name, self.phoneNumber))
    def working(self):
        print("지금 일하고 있음")
    def sleep(self):
        print("지금 잠자고 있음")

#자식 클래스 정의 
class Student(Person):
    #초기화 메서드 재정의(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 초기화 메서드
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
        self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(
        self.subject, self.studentID))

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "230123")
p.printInfo() 
s.printInfo()
