
# %%
# 간단한 리스트 컴프리헨션
[i for i in range(5)]

# %%
# 리스트 컴프리헨션을 전통적인 빈 리스트와
# 반복에서 추가 구문으로 작성
lst = []
for i in range(5):
    lst.append(i)
lst

# %%
# 연산식의 다양한 표현
[i + 1 for i in range(5)]
[i ** 2 for i in range(5)]
[pow(i, 3) for i in range(5)]


# %%
# 컴프리헨션에 추가되는 항목을 리스트와 튜플, 딕셔너리, 집합으로 구성
[[i+1] for i in range(5)]
[(i+1, ) for i in range(5)]
[{i: i**2} for i in range(5)]
[{i+1} for i in range(5)]

# %%
# intro-comp.py
# 간단한 리스트 컴프리헨션
lst1 = [i for i in range(10)]
lst2 = [[i, i+1] for i in range(5)]
lst3 = [{i+1: str(i+1) + '월'} for i in range(5)]

print(lst1)
print(lst2)
print(lst3)

# %%
# 반복 전체의 항목을 리스트에 삽입
[i for i in range(6)]
# 반복 항목 중에서 짝수를 리스트에 삽입
[i for i in range(6) if i%2 == 0]
# 반복 항목 중에서 홀수를 리스트에 삽입
[i for i in range(6) if i%2 == 1]

# %%
# 08-01.py 원 가격에서 할인한 가격 항목을 가지는 리스트 컴프리헨션 
org_grices = [3200, 65000, 43000]
off_rate = .2

## 할인 항목 리스트 컴프리헨션 
final_prices = [i * (1-off_rate) for i in org_grices]
print(final_prices)

## 만원 이상인 가격에 대해 할인 항목 리스트 컴프리헨션 
final_prices = [i * (1-off_rate) for i in org_grices if i >= 10000]
print(final_prices)

# %%
# 08-01.py 소수(prime number)를 출력하는 반복 구문과 소수를 구성하는 리스트 컴프리헨션 
lower, upper = 1, 30
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end = ' ')
else:
    print()

# 소수를 구성하는 리스트 컴프리헨션 
primes = [num for num in range(lower, upper + 1) if (num > 1) & all(num % i != 0 for i in range(2, num))]
print(primes)


# %%
# 조건문
age = 10
if age >= 18:
    adult = '성인'
else:
    adult = '미성년'
    
print(adult)

# %%
# 조건 연산식
age = 10
adult = '성인' if age >= 18 else '미성년'
print(adult)

# %%
# 리스트에 짝수면 0, 홀수면 1을 삽입
[0 if i%2 == 0 else 1 for i in range(10)]

# 리스트에 짝수면 even, 홀수면 odd를 삽입
['even' if i%2 == 0 else 'odd' for i in range(10)]

# %%
# 08-01.py 영어 문자의 대소문자 구분하는 컴프리헨션 
s = 'Python'
lst = ['대' if str.isupper(c) else '소' for c in s]
print(list(s))
print(lst)

## 0은 'zero'로 추가
lst = ['zero' if i == 0 else 'odd' if i%2 == 1 else 'even' for i in range(5)]
print([i for i in range(5)])
print(lst)

# %%
# 고정된 항목의 중첩된 2차원 리스트
[[1] for i in range(3)] # 고정된 항목
[[1, 2] for i in range(3)] # 고정된 항목

# 변화되는 중첩된 2차원 리스트
[[i] for i in range(3)]
[[i, i+1] for i in range(3)]
[[i, i+1, i+2] for i in range(3)]

# 다양한 자료형으로 구성된 리스트의 항목
[(i, i+1) for i in range(4)]
[{i, i+1} for i in range(4)]
[{i: i**2} for i in range(4)]

# %%
# 중첩된 반복을 사용해 생성한 리스트
a = [i + j for i in range(3) for j in range(2)]
print(a)
b = [i * j for i in range(3) for j in range(2)]
print(b)

# 중첩된 반복을 사용해 생성한 항목 딕셔너리로 구성된 리스트
c = [{i: j} for i in range(3) for j in range(2)]
print(c)

# %%
# 중첩된 반복을 사용해 생성한 중첩된 2차원 리스트
a = [[i, j] for i in range(3) for j in range(2)]
b = [[i, j+1] for i in range(3) for j in range(2)]
print(a)
print(b)

# %%
[[0 for col in range(3)] for row in range(2)]
[[1 for col in range(4)] for row in range(3)]

# %%
[[col for col in range(3)] for row in range(2)]
[[col+1 for col in range(4)] for row in range(3)]

# %%
[[col for col in range(row)] for row in range(3)]
[[col for col in range(row, row+2)] for row in range(3)]
[[col for col in range(row, row+4)] for row in range(3)]

# %%
# 행과 열을 정해서 규칙성을 갖는 중첩된 리스트를 생성하는 리스트 컴프리헨션 
ROW= 2
COLUMN = 3
a = [[j for j in range(COLUMN)] for i in range(ROW)]
print(a)

ROW= 2
COLUMN = 4
b = [[i + j for j in range(COLUMN)] for i in range(ROW)]
print(b)

ROW= 4
COLUMN = 3
c = [[i*COLUMN + j for j in range(COLUMN)] for i in range(ROW)]
print(c)

# %%
# dictionary comprehension basics
import math
{i: i*2 for i in range(5)}
{i: i**2 for i in range(5)}
{i: math.sqrt(i) for i in range(5)}

# %%
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k: v*2 for k, v in dict1.items()}
print(double_dict1)

# %%
cubes = {i: pow(i, 3) for i in range(1, 11) if i % 2 == 0}
print(cubes)

# %%
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
reverse_dict1 = {v: k for k, v in dict1.items()}
print(reverse_dict1)

# %%
prime_dict = {num: num > 1 and all (num % i != 0 for i in range(2, int(num**0.5) + 1)) for num in range(2, 11)}
#prime_dict = {num: all(num % i != 0 for i in range(2, int(num**0.5) + 1)) if num > 1 else False for num in range(2, 11)}
print(prime_dict)

from math import sqrt
prime_dict = {num: num > 1 and all (num % i != 0 for i in range(2, int(sqrt(num)) + 1)) for num in range(1, 11)}
print(prime_dict)

'''
2에서 10까지의 정수를 키로 소수 여부(True 또는 False)를 값으로  하는 사전을 생성하는 컴프리헨션 코드 작성 해줘

위 코드에서 range(2, 11)은 2부터 10까지의 정수를 반복합니다. 각 정수 num에 대해서 all(num % i != 0 for i in range(2, int(num**0.5) + 1)) 표현식을 사용하여 소수 여부를 확인합니다. num이 1보다 크면 해당 표현식이 실행되고, 그렇지 않으면 False가 값으로 설정됩니다.

num이 소수인지 확인하기 위해 num을 2부터 num의 제곱근까지의 숫자로 나누어봅니다. 나누어 떨어지는 숫자가 존재하는 경우 소수가 아니므로 False가 되고, 모든 숫자로 나누어 떨어지지 않으면 소수로 판별하여 True가 됩니다.

따라서 출력 결과는 다음과 같이 나타납니다:

yaml
Copy code
{2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False}
위 딕셔너리에서 2, 3, 5, 7은 소수로 True로 표시되었고, 4, 6, 8, 9, 10은 소수가 아니므로 False로 표시되었습니다.

{2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False}
'''

#%%
# 학생의 이름과 성적을 사전으로 만든 리스트
students = [
    {"name": "홍길동", "score": 85},
    {"name": "전지현", "score": 70},
    {"name": "양수경", "score": 95},
    {"name": "김슬기", "score": 65},
    {"name": "김한국", "score": 90}
]

# 성적이 70 이상인 학생은 Pass로, 미만인 학생은 Fail로 값을 지정한 사전 생성
passing_students = {
    student["name"]: "Pass" if student["score"] >= 70 else "Fail"
    for student in students
}
print(passing_students)

# %%
sentence = "hello world"
upper_dict = {char: char.upper() for char in sentence}
print(upper_dict)

#%%
lit = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = {num: True for sublist in lit for num in sublist}
print(flat)

#%%
words = ['apple', 'banana', 'cherry', 'avocado']
first_dict = {word: word[0].upper() for word in words}
print(first_dict)


# %%
# 문자: 코드값으로 구성되는 사전
s = 'python'
chr_dict = {c: ord(c) for c in s}
print(chr_dict)

# 0 ~ 4 정수가 키, 난수로 값을 결정 
from random import randint 
rand_dict = {i: randint(0, i) for i in range(5)}
print(rand_dict)

# words 리스트의 각 단어를 키로 하고 해당 단어의 길이를 값으로 하는 딕셔너리
words = ['apple', 'banana', 'pear']
len_dict = {word: len(word) for word in words}
print(len_dict)

# 주어진 문장에서 각 단어를 키로 하고, 해당 단어의 빈도수를 값으로 하는 딕셔너리를 생성
sentence = "I love Python because Python is versatile"
word_freq = {word: sentence.count(word) for word in sentence.split()}
print(word_freq)

# %%
s = 'abcde'
base = ord('a') - 1
dt1 = {c: ord(c) - base for c in s}
print(dt1)

dt2 = {k: k*2 for k in dt1.keys()}
print(dt2)

dt3 = {v: str(v+1) for v in dt1.values()}
print(dt3)

dt4 = {k: v*2 for (k, v) in dt1.items()}
print(dt4)

# %%
# 1부터 10까지의 짝수를 포함하는 집합 생성
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)  # 출력: {2, 4, 6, 8, 10}

# %%
words = ["apple", "banana", "grape", "orange", "kiwi"]
long_words = {word for word in words if len(word) >= 5}
print(long_words)  # 출력: {'apple', 'banana', 'orange'}

# %%
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)

# %%
sentence = "Lists are a workhorse data type in Python, and many programs manipulate a list at some point."

# 모두 소문자로 변환해서 .과 ,을 제거한 후 단어 리스트를 생성 
words = sentence.lower().replace('.', '').replace(',', '').split()
print(words)

# 문장의 단어를 구성하는 집합 컴프리헨션
unique_words = {word for word in words}
print(unique_words)

# %%
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
        
gen = count_up_to(5)
type(gen)      

# 함수 next()로 제너레이터의 반복 값을 출력
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 모두 반복했으면 오류 발생 
print(next(gen))

# 반복 구문으로 제너테이터 반복 값 출력
gen = count_up_to(5)
for _ in range(5):
    print(next(gen), end= ' ')

# %%
# 0부터 양수이 무한한 짝수를 생성하는 제너레이터 합수
def all_even():
    n = 0
    while True:
        yield n
        n += 2

# 제너레이터 선언
evens = all_even() 
# 천번 호출
for _ in range(1000):
    next(evens)

# 다음 짝수 출력    
print(next(evens))

# %% 연습문제
def fibonacci(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

fibo = fibonacci(10)
for _ in range(10):
    print(next(fibo), end=' ')

# %%
squares = (x**2 for x in range(1, 11))

for _ in range(10):
    print(next(squares), end=' ')

# %%
tri_nums = ((i, i**2, i**3) for i in range(5))    
for _ in range(5):
    print(next(tri_nums))

# %%
nums = (i for i in range(1, 11))    
print(sum(nums))

gen = (i**2 for i in range(1, 11))
print(sum(gen))

# %%
lst = list(i**2 for i in range(10))
print(lst)

cond = all(i < 10 for i in [1, 3, 5, 7])
print(cond)

n_to_s = ", ".join(str(i) for i in range(5))
print(n_to_s)

# %%
import sys

# 리스트 컴프리헨션
list_comp = [x for x in range(1000000)]
# generator 컴프리헨션
gen_comp = (x for x in range(1000000))

print(sys.getsizeof(list_comp))  # 리스트 컴프리헨션의 메모리 사용량 출력
print(sys.getsizeof(gen_comp))   # generator 컴프리헨션의 메모리 사용량 출력

# %%
gen_comp = (x for x in range(10000000))
print(sys.getsizeof(gen_comp))   # generator 컴프리헨션의 메모리 사용량 출력
        


# %%
# map이 도움말로 확인
help(map)

# map에서 내장함수 활용
my_map = map(pow, [1, 2, 3], [2, 2, 2])
my_map
list(my_map)

# map에서 사용자 정의 함수 활용
def my_mult(x, y):
    return x * y

list(map(my_mult, range(1, 5), range(1, 5)))

# map에서 람다 함수 활용
list(map(lambda inch: inch * 2.54, range(6)))

# map에서 메소드 활용
list(map(str.isalpha, 'py13'))

# 내장 함수 int() 인자 하나 또는 둘
int(10)
int('10', 16)

# map에서 내장 함수 int() 활용
list(map(int, [3, 5, 11]))
list(map(int, ['1', '5', '11'], [2, 8, 16]))

# map에서 중첩되게 map() 사용
s = [1, 5, 11]
list(map(str, [1, 5, 11]))
list(map(int, map(str, [1, 5, 11]), [2, 8, 16]))

# map에서 인자인 시퀀스의 수가 잘못된 오류
list(map(lambda x: x+1, [1, 5, 11], [2, 8, 16]))

# 08-01.py 문자열을 역순과 대문자로 변환하는 map()
def my_reverse(s):
    return s[::-1]

langs = ['java', 'python', 'c/c++', 'kotlin']
print(list(map(my_reverse, langs)))

print(list(map(lambda s: s[::-1], langs)))
print(list(map(lambda s: s.upper(), langs)))

print(list(map(str.capitalize, langs)))
print(list(map(str.upper, langs)))

# 08-01.py 콤마가 삽입된 문자열 원화를 정수로 변환
def to_int(num):
    return int(num.replace(",", ""))

wons = ["1,000", "200,000", "3,000,000"]
print(list(map(to_int, wons)))
print(list(map(lambda x: int(x.replace(",", "")), wons)))

# 08-01.py 섭씨와 화씨의 변환
def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9

celsius_temps = [-10, 0, 20, 30, 40]
fahr_temps = [0, 20, 40, 60, 80]
print(list(map(to_fahrenheit, celsius_temps)))
print(list(map(to_celsius, fahr_temps)))

deg1 = list(map(lambda c: 9 / 5 * c + 32, celsius_temps))
deg2 = list(map(lambda f: (f - 32) * 5 / 9, fahr_temps))
print(list(map(lambda x: f'{x:.2f}', deg1)))
print(list(map(lambda x: f'{x:.2f}', deg2)))

## 온도 변환 이후 f'str'로 소수점 이하 3자리만 출력 
print(list(map(lambda c: f'{9 / 5 * c + 32:.3f}', celsius_temps)))
print(list(map(lambda x: f'{(x - 32) * 5 / 9:.3f}', fahr_temps)))

# 08-01.py map()에서 각각의 문자열을 함수 list를 적용
ai = ['tensor', 'pytorch', 'yolo']
 
# map() 각각의 문자열을 리스트로 생성하므로 2차원 리스트 생성
print( list(map(list, ai)) )

####################
# filter()
####################

# %%
even_nums = list(filter(lambda x: x%2 == 0, range(1, 11)))
print(even_nums)  # 출력: [2, 4, 6, 8, 10]

# %%
nums = [-10, 3, 4, -3, 5]
positive_nums = list(filter(lambda x: x > 0, nums))
print(positive_nums)  

# %%
words = ["apple", "banana", "cherry", "date", "day", "elephant"]
filtered_words = list(filter(lambda x: len(x) >= 5, words))
print(filtered_words)  

# %%
# random list
random_list = [1, 'a', 0, '', False, True, '0', 3.4]
filtered_iterator = filter(None, random_list)

#converting to list
filtered_list = list(filtered_iterator)
print(filtered_list)

# %%
# 검사할 단어나 문장
letters = list('python java')

# 문자가 모음이면 True를 반환
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # return True if letter in vowels else False
    return letter in vowels

# 핕터 객체 생성
filtered_vowels = filter(filter_vowels, letters)
# 핕터 객체에서 리스트로 생성
vowels = list(filtered_vowels)
print(vowels) # 리스트 출력

# %% 예제 코드
# 회원 명단
users = [{'mail': 'thomas@gmail.com', 'name': '이 현식', 'gender': 'M'},
         {'mail': 'hint@hotmail.com', 'name': '이 현미', 'gender': 'F'},
         {'mail': 'jjh@gmail.com', 'name': '전 지현', 'gender': 'F'},
         {'mail': 'kiml79@naver.com', 'name': '김 태리', 'gender': 'F'},
         {'mail': 'hskang@naver.com', 'name': '강 한식', 'gender': 'M'}]

# 남성 검사 함수 
def is_man(user):
    return user["gender"] == "M"

# 남성 필터, 출력
for man in filter(is_man, users):
    print(man)
print()

# 여성 필터, 출력
for woman in filter(lambda u: u["gender"] == "F", users):
    print(woman)
print()

# 필터 변수    
filter_mail = filter(lambda u: u["mail"].endswith("@gmail.com"), users)
print(f'filter_mail = {filter_mail}') # 필터 변수 자체 출력    
print(list(filter_mail)) # 필터를 리스트로 생성해 출력
# %%
