class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string문법으로 변수명 그대로 사용 
        print(f'ID: {self.id}, Name: {self.name}')

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f'Title: {self.title}')

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f'Skill: {self.skill}')

# 샘플 데이터 생성
people = [
    Manager(1, 'Alice', 'Project Manager'),
    Employee(2, 'Bob', 'Python'),
    Manager(3, 'Charlie', 'Product Manager'),
    Employee(4, 'David', 'Java'),
    Manager(5, 'Eve', 'HR Manager'),
    Employee(6, 'Frank', 'JavaScript'),
    Manager(7, 'Grace', 'Sales Manager'),
    Employee(8, 'Heidi', 'C++'),
    Manager(9, 'Ivan', 'Operations Manager'),
    Employee(10, 'Judy', 'Ruby')
]

# 정보 출력
for person in people:
    person.printInfo()
    print('---')
