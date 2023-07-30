# %%
def times(a, b):
    return a*b

times
times(4, 5)

# %%
def times(a, b) -> int:
    return a*b

times
times(4, 5)

# %%
def connectURL(server, port):
    strURL = 'https://' + server + ":" + port
    return strURL

print(connectURL('naver.com', '80'))
print(connectURL(port='8080', server='daum.net'))

# %%
g = lambda x, y: x*y
g(2, 3)

# %%
data = 100

# %%
# type hints

# def square(number: union[int, float]) -> union[int, float]:
#     return number ** 2

def square(number: int | float) -> int | float:
    return number ** 2

# %%
# str = 'data'
class GString:
    def __init__(self):
        self.str = ''
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)

g = GString()
g.set('First Message')
g.print()
# %%
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)

# %%
import math
print(math.pi)

import random
print(random.random())



# %% name mangling
class CPrivate():
    def __init__(self, data):
        self.__data = data
    

c = CPrivate(100)
print(c.__dict__)
print(c._CPrivate__data)

# %% type hints

# import Union

def greeting(name: str) -> str:
    return 'Hello ' + name

greeting('Kang')

def greeting(name):
    return 'Hello ' + name

greeting('Park')

# %%
'{}'.format(10)
'{:b}'.format(10)
'{:o}'.format(10)
'{:,}'.format(1500000)

'{:e}'.format(3/4)
'{:.2f}'.format(10)
'{:>20.2f}'.format(10)
'{:<20.2f}'.format(10)
'{:^20.2f}'.format(10)
'{}'.format(10)


# %%
from datetime import *

date(2023, 5, 1)
date(2023, 5, 1)
date(2023, 5, 1)
date.today()
d1 = date.today()
d2 = timedelta(days=100)
d1 + d2 

