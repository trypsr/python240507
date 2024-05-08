# Person2.py 
class Person:
    #클래스 멤버 변수
    num_person = 0 
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))


Person.title = "new title"
p1 = Person()
print("숫자:{0}".format(Person.num_person))
print(p1.title, Person.num_person)

p2 = Person()
print("숫자:{0}".format(Person.num_person))
print(p2.title, Person.num_person)
print(Person.title)


